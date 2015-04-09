# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150407_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='goal',
        ),
    ]
