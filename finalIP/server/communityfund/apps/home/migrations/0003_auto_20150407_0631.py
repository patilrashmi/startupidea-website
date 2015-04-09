# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_projectrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='user',
        ),
        migrations.DeleteModel(
            name='Funding',
        ),
        migrations.AlterField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(related_name='categories_created', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
