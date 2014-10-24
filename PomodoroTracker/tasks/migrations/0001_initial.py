# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=500)),
                ('due_date', models.DateField(blank=True)),
                ('importance', models.PositiveSmallIntegerField(default=2, choices=[(1, b'Not Important'), (2, b'Somewhat Important'), (3, b'Very Important')])),
                ('need_to_happen', models.BooleanField(default=True)),
                ('expected_pomodoros', models.PositiveSmallIntegerField(default=1)),
                ('actual_pomodoros', models.PositiveSmallIntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('day', models.ForeignKey(to='pomodoros.Day', blank=True)),
                ('project', models.ForeignKey(to='tasks.Project', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
