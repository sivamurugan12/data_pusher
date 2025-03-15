from rest_framework import generics
from .models import Role
from .serializers import RoleSerializer

class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
