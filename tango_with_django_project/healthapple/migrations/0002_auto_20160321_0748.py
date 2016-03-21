# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapple', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='person',
            field=models.ForeignKey(default=None, blank=True, to='healthapple.Person', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default=None, blank=True, to='healthapple.Category', null=True),
        ),
    ]
