# Generated by Django 4.1.7 on 2023-03-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_types',
            field=models.CharField(choices=[(1, 'Стая – две единични легла'), (2, 'Апартамент'), (3, 'Стая с двойно легло'), (4, 'Пентхаус'), (5, 'Мезонет')], default=1, max_length=20),
        ),
    ]
