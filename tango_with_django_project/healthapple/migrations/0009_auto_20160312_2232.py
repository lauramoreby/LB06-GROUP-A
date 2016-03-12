# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapple', '0008_auto_20160312_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='flesch_score',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='page',
            name='sentiment_score',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='page',
            name='subjectivity_score',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
        ),
    ]
