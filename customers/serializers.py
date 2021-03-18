from rest_framework import serializers
from .models import Customer


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('manager', 'customer_name', 'address', 'phone', 'photo', 'debt', 'purchases', 'payments', 'id')


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_name', 'address', 'phone', 'photo', 'debt')

    def create(self, validated_data):
        # print("In serializer", validated_data)
        # print("The create func is called")
        manager = self.context.get('manager')
        # print(manager)
        customer = Customer.objects.create(manager=manager, **validated_data)
        customer.save()
        return customer


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('manager', 'customer_name', 'address', 'phone', 'photo', 'debt', 'purchases', 'payments')


class CustomerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_name', 'address', 'phone', 'photo', 'debt', 'purchases', 'payments')


class CustomerActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_name', 'debt', 'purchases', 'payments', 'cumulative_purchases', 'cumulative_payments')

    def update(self, instance, validated_data):
        print(validated_data)
        purchases = validated_data['purchases']
        payments = validated_data['payments']
        instance.debt += purchases - payments
        instance.cumulative_purchases += purchases
        instance.cumulative_payments += payments
        instance.save()
        return instance


class CustomerDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('manager', 'customer_name', 'address', 'phone', 'photo', 'debt', 'purchases', 'payments')
