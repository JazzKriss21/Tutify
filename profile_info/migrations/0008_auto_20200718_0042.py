# Generated by Django 3.0.3 on 2020-07-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_info', '0007_auto_20200717_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='tutorprofile',
            name='availabilty',
            field=models.CharField(default='Both', max_length=50),
        ),
        migrations.AddField(
            model_name='tutorprofile',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to='tutor_proof'),
        ),
        migrations.AddField(
            model_name='tutorprofile',
            name='verfied',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='qualification',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]