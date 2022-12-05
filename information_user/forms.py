import email
from pyexpat import model
from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class InformationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    blood_group = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    birth_date = models.CharField(max_length = 255)
    provinve = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    
    is_admin = models.BooleanField(default = False)
    is_validate = models.BooleanField(default = False)
    by_validate = models.CharField(default = None, max_length = 255)





