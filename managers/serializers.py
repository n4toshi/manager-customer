from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('username', 'first_name', 'last_name', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        manager = Manager(**validated_data)
        manager.set_password(password)
        manager.save()
        return manager

class ManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('username', 'first_name', 'last_name', 'phone', 'id')