from django.db import models
from django.contrib.auth.models import AbstractUser
from .Manager import userManager

class CustomUser(AbstractUser):
    phone = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=300, null=True, blank=True )
    profile_img = models.ImageField(upload_to='profile', null=True, blank=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = userManager
    def __str__(self):
        return self.email