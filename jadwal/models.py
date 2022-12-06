from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Jadwal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    loc = models.TextField()
    accepted = models.TextField()