from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    upload = models.ForeignKey(User, null=True,related_name="codingdojo", on_delete=models.PROTECT)
    users = models.ManyToMfanyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)