# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-06 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0010_answer_que_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='author_ans',
            new_name='author',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='que',
            field=models.TextField(null=True),
        ),
    ]