from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import make_password
from django import forms


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         self.password = make_password(self.password, None, 'pbkdf2_sha256')
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         extra_fields.setdefault('is_staff', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         self.password = make_password(self.password, None, 'pbkdf2_sha256')
#         return self._create_user(email, password, **extra_fields)

class UserManager(BaseUserManager):
    use_in_migrations = True

    # Method to save user to the database
    def save_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # Call this method for password hashing
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False
        return self.save_user(email, password, **extra_fields)

    # Method called while creating a staff user
    def create_staffuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = False
        
        return self.save_user(email, password, **extra_fields) 

    # Method called while calling creatsuperuser
    def create_superuser(self, email, password, **extra_fields):

        # Set is_superuser parameter to true
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser should be True')
        
        extra_fields['is_staff'] = True

        return self.save_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,max_length=225)
    first_name=models.CharField(max_length=225)
    last_name = models.CharField( max_length=225, blank=True)
    date_joined = models.DateTimeField( auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



currency_choice =(
    ("EUR/USD", "EUR/USD"),
    ("USD/JPY", "USD/JPY"),
    ("GBP/USD", "GBP/USD"),
    ("USD/CAD", "USD/CAD"),
    ("USD/HKD", "USD/HKD"),
    ("USD/CNY", "USD/CNY"),
    ("AUD/USD", "AUD/USD"),
    ("USD/GHS", "USD/GHS"),
    ("EUR/GHS", "EUR/GHS"),
    ("JPY/GHS", "JPY/GHS"),
    ("USD/GHS", "USD/GHS"),
    ("CAD/GHS", "CAD/GHS"),
    ("HKD/GHS", "HKD/GHS"),
    ("CNY/GHS", "CNY/GHS"),
    ("AUD/GHS", "AUD/GHS"),
)

action_choice =(
    ("buy", "buy"),
    ("sell", "sell"),
)


class Signal(models.Model):
    currency = forms.ChoiceField(choices = currency_choice)
    action = forms.ChoiceField(choices = action_choice)
    start_value = models.CharField(max_length=255)
    end_value = models.TextField(max_length=225)
    created = models.DateTimeField(auto_now=True, verbose_name="date created")
    class Meta:
        ordering = ['created']
