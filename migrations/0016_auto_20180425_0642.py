# Generated by Django 2.0.3 on 2018-04-25 06:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0015_auto_20180425_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='BnbaTwsel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nop', models.CharField(max_length=50)),
                ('no_rumah', models.CharField(max_length=50)),
                ('lingkungan', models.CharField(max_length=50)),
                ('kode_foto', models.CharField(max_length=50, null=True)),
                ('stat', models.CharField(max_length=50)),
                ('path_foto', models.CharField(max_length=50, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32651)),
            ],
            options={
                'verbose_name': 'Titiwungen Selatan',
            },
        ),
    ]
