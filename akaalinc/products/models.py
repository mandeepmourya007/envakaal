
from django.db import models

class add_product(models.Model):
    name = models.CharField(max_length=100)
    detail=models.TextField()
    pdf_file =  models.FileField(upload_to='pdfs/', null=True, blank=True)
    image=models.FileField(null=True,blank=True,upload_to="static/pythimages")
    def __str__(self):
        return self.name

from django.contrib import admin
from .models import add_product
admin.site.register(add_product)

# Create your models here.
