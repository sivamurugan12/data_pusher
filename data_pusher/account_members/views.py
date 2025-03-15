from rest_framework import generics
from .models import AccountMember
from .serializers import AccountMemberSerializer
from rest_framework.permissions import IsAuthenticated

class AccountMemberListCreateView(generics.ListCreateAPIView):
    queryset = AccountMember.objects.all()
    serializer_class = AccountMemberSerializer
    permission_classes = [IsAuthenticated]

class AccountMemberRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountMember.objects.all()
    serializer_class = AccountMemberSerializer
    permission_classes = [IsAuthenticated]
