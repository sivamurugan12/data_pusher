from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    secret_token = models.CharField(max_length=64, unique=True, editable=False)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_accounts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_accounts')

    def __str__(self):
        return self.name
