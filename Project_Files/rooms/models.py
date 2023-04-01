from django.db import models

ROOM_TYPES = [
    (1, 'Стая – две единични легла'),
    (2, 'Апартамент'),
    (3, 'Стая с двойно легло'),
    (4, 'Пентхаус'),
    (5, 'Мезонет'),
]


class Room(models.Model):
    capacity = models.IntegerField()  # number of people
    room_types = models.IntegerField(choices=ROOM_TYPES)
    is_Free = models.BooleanField()
    Description = models.TextField(default="(Description here)")
    Price = models.FloatField()
