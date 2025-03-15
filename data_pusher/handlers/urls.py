from django.urls import path
from .views import ReceiveDataView

urlpatterns = [
    path('incoming_data/', ReceiveDataView.as_view(), name='receive-data'),
]
