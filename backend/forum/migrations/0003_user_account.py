# Generated by Django 2.0 on 2018-06-04 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20180604_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.OneToOneField(default='315010000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
