from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     pass

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return 'User: ' + self.user.username # this will be shown in the database as a link to the actual record
