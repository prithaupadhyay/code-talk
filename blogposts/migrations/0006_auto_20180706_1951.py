# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-06 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0005_auto_20180706_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='que_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
