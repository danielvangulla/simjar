# Generated by Django 2.0.3 on 2018-05-25 06:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0034_bnbaranomuut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infralampu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, null=True)),
                ('descript', models.CharField(max_length=254, null=True)),
                ('type', models.CharField(max_length=254, null=True)),
                ('comment', models.CharField(max_length=254, null=True)),
                ('symbol', models.CharField(max_length=254, null=True)),
                ('elevation', models.FloatField(null=True)),
                ('date_time_field', models.CharField(max_length=50, null=True)),
                ('keterangan', models.CharField(max_length=8, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(null=True, srid=32651)),
            ],
            options={
                'verbose_name': 'Infrastruktur Lampu Jalan',
            },
        ),
    ]
