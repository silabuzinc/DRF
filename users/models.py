from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    realname = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)