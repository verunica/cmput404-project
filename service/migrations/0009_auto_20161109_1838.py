# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20161102_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='friends',
        ),
        migrations.AddField(
            model_name='author',
            name='friends',
            field=models.ManyToManyField(related_name='_author_friends_+', to='service.Author'),
        ),
    ]
