# Generated by Django 2.1.7 on 2019-03-15 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_videogame_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='user',
        ),
    ]