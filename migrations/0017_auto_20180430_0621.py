# Generated by Django 2.0.3 on 2018-04-30 06:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0016_auto_20180425_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='BnbaCal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rumah', models.CharField(max_length=50)),
                ('nop', models.CharField(max_length=50)),
                ('lingkungan', models.CharField(max_length=50)),
                ('kode_foto', models.CharField(max_length=50, null=True)),
                ('stat', models.CharField(max_length=50)),
                ('path_foto', models.CharField(max_length=50, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32651)),
            ],
            options={
                'verbose_name': 'Calaca',
            },
        ),
    ]
