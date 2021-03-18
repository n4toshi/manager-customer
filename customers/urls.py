from django.urls import path
from .views import CustomerListView, CustomerCreate, CustomerDetail, CustomerEdit, CustomerAction, CustomerDelete


urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('create/', CustomerCreate.as_view(), name='customer_create'),
    path('<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
    path('edit/<int:pk>/', CustomerEdit.as_view(), name='customer_edit'),
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='customer_delete'),
    path('action/<int:pk>/', CustomerAction.as_view(), name='customer_action'),
]