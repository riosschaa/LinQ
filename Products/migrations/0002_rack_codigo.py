# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-21 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='codigo',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]