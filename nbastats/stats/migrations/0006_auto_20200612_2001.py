# Generated by Django 3.0.6 on 2020-06-12 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20200604_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='first_season',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_season',
        ),
    ]
