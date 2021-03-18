from django.urls import path
from .views import ManagerCreate, ManagerListView

urlpatterns = [
    path('register/', ManagerCreate.as_view(), name='register'),
    path('list/', ManagerListView.as_view(), name='manager_list'),
]