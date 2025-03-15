from django.urls import path
from .views import LogListView, LogDetailView

urlpatterns = [
    path('', LogListView.as_view(), name='log-list'),
    path('<int:pk>/', LogDetailView.as_view(), name='log-detail'),
]
