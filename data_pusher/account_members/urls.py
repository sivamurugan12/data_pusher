from django.urls import path
from .views import AccountMemberListCreateView, AccountMemberRetrieveUpdateDeleteView

urlpatterns = [
    path('', AccountMemberListCreateView.as_view(), name='account-member-list-create'),
    path('<int:pk>/', AccountMemberRetrieveUpdateDeleteView.as_view(), name='account-member-detail'),
]
