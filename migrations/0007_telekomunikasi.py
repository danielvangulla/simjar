# Generated by Django 2.0.3 on 2018-03-13 14:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0006_trtrayek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telekomunikasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.FloatField()),
                ('menara', models.CharField(max_length=254)),
                ('longitude', models.FloatField()),
                ('lattitude', models.FloatField()),
                ('antena_hei', models.FloatField()),
                ('site_categ', models.CharField(max_length=254)),
                ('desa', models.CharField(max_length=254)),
                ('kecamatan', models.CharField(max_length=254)),
                ('kabupaten', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32651)),
            ],
            options={
                'verbose_name': 'BTS Telekomunikasi',
            },
        ),
    ]
