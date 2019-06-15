from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_user_id = models.CharField(max_length=100, unique=True)
    picture = models.TextField()
    token = models.CharField(max_length=200, unique=True)
