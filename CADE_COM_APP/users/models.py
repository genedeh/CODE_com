from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=8, unique=True)
    email = models.EmailField(default='')
    profile_image = models.ImageField(default="User_Image/no_profile_image.jpg", unique=True)
    description = models.TextField(max_length=1000, blank=True, default='')

    def __str__(self):
        return f'{self.username}'
