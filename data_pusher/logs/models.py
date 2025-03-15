from django.db import models
from accounts.models import Account
from destinations.models import Destination
import uuid

class Log(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    received_timestamp = models.DateTimeField(auto_now_add=True)
    processed_timestamp = models.DateTimeField(null=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    received_data = models.JSONField()
    status = models.CharField(max_length=10, choices=[('success', 'Success'), ('failed', 'Failed')])

    def __str__(self):
        return f"Event {self.event_id} - {self.status}"
