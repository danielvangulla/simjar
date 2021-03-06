# Generated by Django 2.0.3 on 2018-03-13 14:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0005_trjembatan'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrTrayek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panjang_km', models.FloatField()),
                ('nama_traye', models.CharField(max_length=254)),
                ('kode_traye', models.CharField(max_length=254)),
                ('rute', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=32651)),
            ],
            options={
                'verbose_name': 'Trayek',
            },
        ),
    ]
