# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('summary', models.CharField(default=b'', max_length=128)),
                ('url', models.URLField()),
                ('flesch_score', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('polarity_score', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('subjectivity_score', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('category', models.ForeignKey(default=None, blank=True, to='healthapple.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=None, upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='person',
            field=models.ForeignKey(default=None, blank=True, to='healthapple.Person', null=True),
            preserve_default=True,
        ),
    ]
