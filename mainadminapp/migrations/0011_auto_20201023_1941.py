# Generated by Django 2.2 on 2020-10-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainadminapp', '0010_auto_20201023_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booki',
            name='adamount',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='booki',
            name='balanceamount',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='booki',
            name='noofadults',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booki',
            name='payementmode',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='booki',
            name='totalamount',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
