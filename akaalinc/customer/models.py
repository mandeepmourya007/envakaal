from django.db import models



class customer_details(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=80,default="")
    phone_number =  models.CharField(max_length=20)
    message=models.TextField()
    def __str__(self):
        return self.name

from django.contrib import admin
from .models import customer_details
admin.site.register(customer_details)

# Create your models here.
