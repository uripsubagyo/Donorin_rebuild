from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class InformationUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)    #include username, email, passwords
    full_name = models.CharField(max_length = 100)
    blood_group = models.CharField(max_length = 3)
    phone_number = models.CharField(max_length = 15)
    birth_date = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)

    is_validate = models.BooleanField(default = False)              # untuk diverifikasi oleh admin
    is_admin_user = models.BooleanField(default= False)             # untuk membedakan relawan dan staff admin
    by_validate = models.CharField(max_length = 30, default="none")
    
    def is_admin(self):
        return self.is_admin_user
    
    def is_validate(self):
        return self.is_validate