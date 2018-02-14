# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('periodicals', '0027_add_title_image_to_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodicals.ArticleType'),
        ),
    ]
