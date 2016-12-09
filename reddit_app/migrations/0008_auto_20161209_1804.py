# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 18:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit_app', '0007_auto_20161207_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reddit_app.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='commentvote',
            unique_together=set([('user', 'comment')]),
        ),
    ]