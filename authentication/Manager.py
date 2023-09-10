from django.contrib.auth.base_user import BaseUserManager

class userManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_field):
        if not phone:
            raise ValueError('phone is required')
        user = self.model(phone=phone, **extra_field)
        # user = self.normalize_email('email')
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone,username, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)
        return self.create_user(phone, password, **extra_field)

