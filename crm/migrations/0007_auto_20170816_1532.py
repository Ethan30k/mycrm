# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20170816_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classlist',
            old_name='name',
            new_name='course',
        ),
    ]