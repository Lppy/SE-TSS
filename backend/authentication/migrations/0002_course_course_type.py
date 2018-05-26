# Generated by Django 2.0 on 2018-05-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.PositiveSmallIntegerField(choices=[(0, '公共课'), (1, '专业选修课'), (2, '专业必修课')], default=0, verbose_name='课程类别'),
            preserve_default=False,
        ),
    ]
