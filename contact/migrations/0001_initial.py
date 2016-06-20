# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-20 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=52)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]