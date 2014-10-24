# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoros', '0002_auto_20141024_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodoro',
            name='tasks',
            field=models.ManyToManyField(to='tasks.Task', null=True, blank=True),
            preserve_default=True,
        ),
    ]
