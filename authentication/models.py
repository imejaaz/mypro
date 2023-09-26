from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from .Manager import userManager
from django.dispatch import receiver
from django.http import HttpResponse
from django.db.models.signals import post_save

class MyUser(AbstractUser, PermissionsMixin):
    username =  None
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(upload_to='authentication', null=True, blank=True)

    objects = userManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email

@receiver(post_save, sender=MyUser)
def new_user_signup(sender, instance, created, **kwargs):
    if created:
        response_text = "User created successfully!"
        # You can modify this response as needed
        print(response_text)