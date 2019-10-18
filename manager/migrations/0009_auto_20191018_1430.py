# Generated by Django 2.2.5 on 2019-10-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20191018_1413'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReturnedOrder',
        ),
        migrations.AddField(
            model_name='rentorder',
            name='is_returned',
            field=models.BooleanField(default=False, verbose_name='是否归还'),
        ),
        migrations.AddField(
            model_name='rentorder',
            name='return_date',
            field=models.DateField(blank=True, default=None, verbose_name='归还日期'),
        ),
        migrations.AlterField(
            model_name='rentorder',
            name='phone',
            field=models.IntegerField(verbose_name='电话号码'),
        ),
    ]
