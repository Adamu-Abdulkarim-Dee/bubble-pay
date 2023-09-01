from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings
from .choices import *

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)

class Bvn(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bank_verification_number = models.IntegerField()
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    surename = models.CharField(max_length=50)

class Nin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    surename = models.CharField(max_length=50)
    national_identifation_number = models.IntegerField()

class UserInformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    local_government = models.CharField(max_length=100)
    

class NextOfKin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=100)