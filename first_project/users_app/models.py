from django.db import models

# Create your models here.

class users(models.Model):
    firstName = models.CharField(max_length = 264)
    lastName = models.CharField(max_length = 264)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.firstName
