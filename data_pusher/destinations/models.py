from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Account

User = get_user_model()

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    http_method = models.CharField(max_length=10, choices=[('GET', 'GET'), ('POST', 'POST')])
    headers = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_destinations')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_destinations')

    def __str__(self):
        return f"{self.account.name} - {self.url}"
