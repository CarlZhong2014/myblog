# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-19 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='symbol',
            new_name='en_name',
        ),
        migrations.AddField(
            model_name='catagory',
            name='nav_status',
            field=models.BooleanField(default=True, verbose_name='\u5bfc\u822a\u9879'),
        ),
    ]
