# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('poll_id', models.AutoField(primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=160)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('author_privacy', models.CharField(choices=[('A', 'Anonymous'), ('N', 'NameOnly'), ('NE', 'NameAndEmail')], max_length=2)),
                ('vote_access', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('DEFAULT', 'DEFAULT'), ('PROTECTED', 'PROTECTED'), ('PRIV4', 'PRIVATE')], max_length=3)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('invited_voters', models.ManyToManyField(related_name='invited_voters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('choice_selected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
    ]
