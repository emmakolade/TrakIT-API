from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
# creating a custom user model


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('users should have an email')
        # define how  a user sould be created
        user = self.model(username=username, email=self.normalize_email(email))
        user.password = make_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('password should be provided')
        # define how  a superuser sould be created
        user = self.create_user(username, email, password)
        user = self.model(username=username, email=self.normalize_email(email))
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # define what the user will use to sign in 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects =UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    