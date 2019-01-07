# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 06:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app01', '0002_auto_20190105_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='dianpu',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dp_money',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dp_project',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shengfen',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xqdz',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
            preserve_default=False,
        ),
    ]