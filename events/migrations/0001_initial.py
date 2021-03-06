# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-26 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=500, unique=True)),
                ('map_url', models.URLField(max_length=1000)),
            ],
        ),
    ]
