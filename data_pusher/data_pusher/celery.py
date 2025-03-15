from urllib import request
from celery import Celery

from destinations.models import Destination

app = Celery('data_pusher', broker='redis://localhost:6379/0')

@app.task
def send_data(destination_id, data):
    destination = Destination.objects.get(id=destination_id)
    request.post(destination.url, json=data, headers=destination.headers)
