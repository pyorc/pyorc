# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('image_url', models.CharField(max_length=128, null=True)),
                ('author', models.CharField(max_length=32)),
                ('date_time', models.DateTimeField()),
                ('keywords', models.CharField(max_length=128, null=True)),
                ('original_link', models.CharField(max_length=128)),
                ('source', models.CharField(max_length=16)),
                ('content', models.TextField()),
                ('reading_number', models.IntegerField(default=0)),
                ('agree_number', models.IntegerField(default=0)),
                ('disagree_number', models.IntegerField(default=0)),
                ('category', models.IntegerField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
