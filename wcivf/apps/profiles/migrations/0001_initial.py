# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0007_personpost_election'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('person_post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='people.PersonPost')),
                ('text', models.TextField(blank=True)),
                ('url', models.CharField(blank=True, max_length=800)),
            ],
        ),
    ]