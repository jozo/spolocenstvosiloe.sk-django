# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
    ]