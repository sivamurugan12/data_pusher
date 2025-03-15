from django.urls import path
from .views import AccountListCreateView, AccountRetrieveUpdateDeleteView

urlpatterns = [
    path('', AccountListCreateView.as_view(), name='account-list-create'),
    path('<uuid:pk>/', AccountRetrieveUpdateDeleteView.as_view(), name='account-detail'),
]
