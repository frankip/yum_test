# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedform', '0002_auto_20171001_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='name',
        ),
        migrations.AddField(
            model_name='details',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]