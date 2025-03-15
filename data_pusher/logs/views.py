from rest_framework import generics
from .models import Log
from .serializers import LogSerializer

class LogListView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogDetailView(generics.RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
