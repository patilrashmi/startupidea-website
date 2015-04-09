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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('creator', models.ForeignKey(related_name='communities_created', to=settings.AUTH_USER_MODEL)),
                ('subscribers', models.ManyToManyField(related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('amount', models.PositiveIntegerField()),
                ('funded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=100)),
                ('summary', models.TextField(max_length=250)),
                ('description', models.TextField(max_length=20000)),
                ('goal', models.PositiveIntegerField()),
                ('deadline', models.DateTimeField()),
                ('category', models.ForeignKey(related_name='ideas', to='home.Category')),
                ('initiator', models.ForeignKey(related_name='ideas_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='funding',
            name='idea',
            field=models.ForeignKey(related_name='fundings', to='home.Idea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='funding',
            name='user',
            field=models.ForeignKey(related_name='fundings', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
