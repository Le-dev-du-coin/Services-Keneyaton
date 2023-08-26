from django.db import models
from django.contrib.auth.models import AbstractUser



class Account(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)

    # Required 
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email