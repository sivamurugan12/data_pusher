from rest_framework import serializers
from .models import AccountMember

class AccountMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMember
        fields = '__all__'
