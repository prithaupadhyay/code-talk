# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-08 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0012_auto_20180707_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_que',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
