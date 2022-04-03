from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

GENDER_CHOICES = (('female', 'Female'), ('male', 'Male'))


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """Creates and saver a new superuser"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Patient(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def birth_date_formate(self):
        return self.birth_date.strftime('%d/%m/%Y')
