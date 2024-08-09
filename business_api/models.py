from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=250)
    user_id = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    email = models.EmailField()


class Transaction(models.Model):
    reference = models.CharField(max_length=250, null=True, blank=True)
    choices = (
        ("ishare", "ishare"),
        ("mtn_flexi", "mtn_flexi"),
        ("big-time", "big-time"),
        ("top_up", "top_up")
    )
    transaction_type = models.CharField(max_length=250, choices=choices, null=True, blank=True)
    date = models.DateField(auto_now_add=True)


class Blacklist(models.Model):
    phone_number = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.phone_number
