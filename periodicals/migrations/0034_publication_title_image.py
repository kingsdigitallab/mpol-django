# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodicals', '0033_periodical_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='title_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
