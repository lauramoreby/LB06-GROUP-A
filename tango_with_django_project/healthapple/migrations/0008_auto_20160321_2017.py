# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapple', '0007_auto_20160321_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'profile_images', blank=True),
        ),
    ]
