from django.urls import path
from .views import UserCreateView, UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('register/', UserCreateView.as_view(), name='user-register'),
]
