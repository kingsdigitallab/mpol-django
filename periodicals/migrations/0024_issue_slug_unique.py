# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodicals', '0023_issue_slug_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
