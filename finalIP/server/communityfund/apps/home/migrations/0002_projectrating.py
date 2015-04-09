# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('positive', models.BooleanField(default=True)),
                ('idea', models.ForeignKey(to='home.Idea', related_name='ratings')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='idea_ratings')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
