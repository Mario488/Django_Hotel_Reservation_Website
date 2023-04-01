from django.db import models

# Create your models here.
class Reservations(models.Model):
    reserved_room = models.IntegerField()
    username = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    including_breakfast = models.BooleanField()
    all_inclusive = models.BooleanField()
    cost = models.FloatField()