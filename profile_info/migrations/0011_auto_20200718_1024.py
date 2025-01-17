# Generated by Django 3.0.3 on 2020-07-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_info', '0010_auto_20200718_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorprofile',
            old_name='user',
            new_name='account',
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='availabilty',
            field=models.CharField(blank=True, default='Both', max_length=50),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
