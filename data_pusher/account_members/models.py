from django.db import models
from users.models import CustomUser
from accounts.models import Account

class AccountMember(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_members')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='account_memberships')
    role_id = models.IntegerField(choices=[(1, 'Admin'), (2, 'Normal User')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_account_members')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='updated_account_members')

    def __str__(self):
        return f"{self.user.username} - {self.account.name} ({self.get_role_id_display()})"
