from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address=models.TextField(blank=True,null=True)
    description= models.TextField(blank=True,null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
