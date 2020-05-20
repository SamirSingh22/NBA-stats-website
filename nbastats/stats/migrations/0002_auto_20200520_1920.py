# Generated by Django 3.0.6 on 2020-05-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='season',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='apg',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ppg',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rpg',
        ),
        migrations.AddField(
            model_name='player',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='player_id',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
