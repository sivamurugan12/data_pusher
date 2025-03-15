from django.urls import path
from .views import DestinationListCreateView, DestinationRetrieveUpdateDeleteView

urlpatterns = [
    path('', DestinationListCreateView.as_view(), name='destination-list-create'),
    path('<int:pk>/', DestinationRetrieveUpdateDeleteView.as_view(), name='destination-detail'),
]
