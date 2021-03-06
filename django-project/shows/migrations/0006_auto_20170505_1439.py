# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_auto_20170504_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='showcategory',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='show',
            name='overall_order',
            field=models.IntegerField(default=0, verbose_name='Overall Ordering - Use instead of per item.'),
        ),
        migrations.AlterField(
            model_name='showcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='shows.Category'),
        ),
        migrations.AlterField(
            model_name='showcategory',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Nonfunctional Order'),
        ),
        migrations.AlterField(
            model_name='showcategory',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='shows.Show'),
        ),
    ]
