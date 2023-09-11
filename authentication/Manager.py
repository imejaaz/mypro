from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class userManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), password = password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):

        email= self.normalize_email(email)
        user = self.create_user(email,password)
        # user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
