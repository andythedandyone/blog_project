# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161022_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='/blog/'),
        ),
    ]
