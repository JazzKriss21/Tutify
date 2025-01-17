# Generated by Django 3.0.3 on 2020-07-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_info', '0009_auto_20200718_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='subjects',
            field=models.TextField(blank=True),
        ),
    ]
