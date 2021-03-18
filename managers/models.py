from django.contrib.auth.models import AbstractUser
from django.db import models


class Manager(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)    
    phone = models.CharField(max_length=25)
    registered_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['password', 'password2']

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'