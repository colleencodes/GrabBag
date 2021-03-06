# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('link', models.URLField(max_length=500)),
                ('photo', models.ImageField(upload_to='gift_pics')),
            ],
            options={
                'db_table': 'gift',
            },
        ),
    ]
