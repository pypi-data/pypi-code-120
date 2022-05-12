from paradoxdjango.contrib.auth.base_user import AbstractBaseUser
from paradoxdjango.contrib.auth.models import BaseUserManager
from paradoxdjango.db import models


class CustomEmailFieldUserManager(BaseUserManager):
    def create_user(self, username, password, email):
        user = self.model(username=username)
        user.set_password(password)
        user.email_address = email
        user.save(using=self._db)
        return user


class CustomEmailField(AbstractBaseUser):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email_address = models.EmailField(null=True)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = "email_address"
    USERNAME_FIELD = "username"

    objects = CustomEmailFieldUserManager()
