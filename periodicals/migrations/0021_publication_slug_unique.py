# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodicals', '0020_publication_slug_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(max_length=3, unique=True),
        ),
    ]
