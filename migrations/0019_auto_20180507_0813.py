# Generated by Django 2.0.3 on 2018-05-07 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpuljaringan', '0018_auto_20180507_0744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bnbaistq',
            old_name='Status',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='bnbakl',
            old_name='Status',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='bnbamhkt',
            old_name='Status',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='bnbapin',
            old_name='Status',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='bnbatelb',
            old_name='Status',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='bnbatklak',
            old_name='Status',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='bnbawngsel',
            old_name='Status',
            new_name='stat',
        ),
    ]
