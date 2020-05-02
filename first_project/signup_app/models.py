####### sorry this file was accidentally changed.  #######


from django.db import models

# Create your models here.

class new_user(models.Model):
    name = models.CharField(max_length = 264)
    password = models.CharField(max_length = 264)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
