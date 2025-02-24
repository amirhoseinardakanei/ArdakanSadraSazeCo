from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    national_number = models.CharField(max_length=10, verbose_name='کد ملی')


    def get_full_name(self):

        return self.first_name + ' ' + self.last_name

