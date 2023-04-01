from django.db import models
from django.core.validators import RegexValidator, EmailValidator

# Create your models here.
class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$', 'EGN must contain only digits')
    ])
    email = models.EmailField(validators=[EmailValidator()])
    

