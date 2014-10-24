# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        ('pomodoros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomodoro',
            name='tasks',
            field=models.ManyToManyField(to='tasks.Task', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='distraction',
            name='pomodoro',
            field=models.ForeignKey(to='pomodoros.Pomodoro'),
            preserve_default=True,
        ),
    ]
