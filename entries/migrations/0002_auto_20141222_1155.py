# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='author',
        ),
    ]
