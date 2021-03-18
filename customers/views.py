from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Customer
from .pagination import ListPagination
from .serializers import CustomerListSerializer, CustomerCreateSerializer, CustomerDetailSerializer, CustomerEditSerializer, CustomerActionSerializer, CustomerDeleteSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from managers.models import Manager
from .permissions import IsHisManagerPermission


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer
    pagination_class = ListPagination
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('customer_name', 'manager')
    search_fields = ('customer_name', 'manager')


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomerCreateSerializer

    def get_serializer_context(self):
        context = super(CustomerCreate, self).get_serializer_context()
        context.update({'manager': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        context = self.request.data
        print("context request data", context, 'request.user', self.request.user)
        return self.create(request, manager=self.request.user, *args, **kwargs)


class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class CustomerEdit(generics.RetrieveUpdateAPIView):
    permission_classes = (IsHisManagerPermission, )
    queryset = Customer.objects.all()
    serializer_class = CustomerEditSerializer


class CustomerAction(generics.RetrieveUpdateAPIView):
    permission_classes = (IsHisManagerPermission, )
    queryset = Customer.objects.all()
    serializer_class = CustomerActionSerializer

    def put(self, request, *args, **kwargs):
        purchases = request.data['purchases']
        payments = request.data['payments']
        if not purchases.isdigit():
            raise Exception("The purchases column expected an amount in KGS.")
        else:
            pass
        if not payments.isdigit():
            raise Exception("The payments column expected an amount in KGS.")
        elif int(payments) < 0:
            raise Exception("The payments column cannot be filled with a negative amount.")
        else:
            pass
        return self.update(request, *args, **kwargs)



    def patch(self, request, *args, **kwargs):
        purchases = request.data['purchases']
        payments = request.data['payments']
        if not purchases.isdigit():
            raise Exception("The purchases column expected an amount in KGS.")
        else:
            pass
        if not payments.isdigit():
            raise Exception("The payments column expected an amount in KGS.")
        elif int(payments) < 0:
            raise Exception("The payments column cannot be filled with a negative amount.")
        else:
            pass
        return self.partial_update(request, *args, **kwargs)


class CustomerDelete(generics.RetrieveDestroyAPIView):
    permission_classes = (IsHisManagerPermission, )
    queryset = Customer.objects.all()
    serializer_class = CustomerDeleteSerializer