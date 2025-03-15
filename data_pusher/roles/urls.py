from django.urls import path
from .views import RoleListView

urlpatterns = [
    path('', RoleListView.as_view(), name='role-list'),
]
