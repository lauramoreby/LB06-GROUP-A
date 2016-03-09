# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapple', '0002_remove_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=None, to='healthapple.UserProfile'),
            preserve_default=True,
        ),
    ]
