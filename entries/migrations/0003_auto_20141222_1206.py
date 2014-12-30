# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20141222_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 18, 6, 17, 81129, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 18, 6, 32, 43984, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 18, 6, 37, 528298, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
