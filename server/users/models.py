from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', max_length=50, unique=True)
    first_name = models.CharField('first name', max_length=50, blank=True)
    last_name = models.CharField('last name', max_length=50, blank=True)
    is_active = models.BooleanField('active', default=True)

    created_at = models.DateTimeField('date joined', auto_now_add=True)
    updated_at = models.DateTimeField('when updated', auto_now=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



