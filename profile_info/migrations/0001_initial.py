# Generated by Django 3.0.3 on 2020-03-25 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profile_info.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('subjects', models.TextField()),
                ('qualification', models.CharField(max_length=256)),
                ('bio', models.TextField(max_length=5000)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=profile_info.models.upload_location)),
                ('hourly_rate', models.IntegerField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]