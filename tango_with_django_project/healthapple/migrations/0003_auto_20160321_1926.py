# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapple', '0002_auto_20160321_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(height_field=100, width_field=100, upload_to=b'profile_images', blank=True),
        ),
    ]
