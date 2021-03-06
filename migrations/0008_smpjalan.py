# Generated by Django 2.0.3 on 2018-03-13 14:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0007_telekomunikasi'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmpJalan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_x', models.FloatField()),
                ('point_y', models.FloatField()),
                ('nama_obyek', models.CharField(max_length=254)),
                ('kls_obyek', models.CharField(max_length=254)),
                ('kode', models.CharField(max_length=254)),
                ('no_foto', models.CharField(max_length=254)),
                ('tgl_surv', models.CharField(max_length=254)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32651)),
            ],
            options={
                'verbose_name': 'Sempadan Jalan',
            },
        ),
    ]
