# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-13 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitt',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
