# Generated by Django 2.2.5 on 2019-10-18 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_auto_20191018_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentorder',
            name='return_date',
        ),
    ]
