from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# creating a custom user model 
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('users should have an email')
        # define how  a user sould be created
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        
    def create_user(self, username, email, password=None):
        if password is None:
            raise TypeError('password should be provided')
        if email is None:
            raise TypeError('users should have an email')
        # define how  a user sould be created
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()