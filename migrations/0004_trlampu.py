# Generated by Django 2.0.3 on 2018-03-13 13:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0003_patchsulut'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrLampu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32651)),
            ],
            options={
                'verbose_name': 'Lampu Lalu Lintas',
            },
        ),
    ]
