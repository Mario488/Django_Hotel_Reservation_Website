from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(validators=[EmailValidator()])
