from celery import shared_task
import requests
from .models import Logs, Destinations, Accounts

@shared_task
def send_data_async(account_id, event_id, data):
    """
    Asynchronous task to send data to all linked destinations of an account.
    Logs each request after processing.
    """
    try:
        account = Accounts.objects.get(id=account_id)
        destinations = Destinations.objects.filter(account=account)
        
        for destination in destinations:
            headers = {
                "Content-Type": "application/json",
                "CL-X-EVENT-ID": event_id
            }
            
            response = requests.post(destination.url, json=data, headers=headers)
            status = "success" if response.status_code == 200 else "failed"
            
            # Log the request
            Logs.objects.create(
                event_id=event_id,
                account=account,
                destination=destination,
                received_data=data,
                status=status
            )
        
        return "Data sent successfully to destinations."
    except Accounts.DoesNotExist:
        return "Account not found."
    except Exception as e:
        return f"Error processing data: {str(e)}"
