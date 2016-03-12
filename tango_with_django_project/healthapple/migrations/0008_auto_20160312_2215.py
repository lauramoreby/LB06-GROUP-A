# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapple', '0007_auto_20160310_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='user',
            new_name='person',
        ),
    ]
