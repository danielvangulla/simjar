# Generated by Django 2.0.3 on 2018-05-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0021_auto_20180508_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnbapin',
            name='kode_kec',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='bnbapin',
            name='kode_kel',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='bnbapin',
            name='trans_id',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='bnbapin',
            name='upk',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
