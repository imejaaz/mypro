from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from .Manager import userManager


class MyUser(AbstractUser, PermissionsMixin):
    username =  None
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_admin = models.BooleanField()

    objects = userManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email

