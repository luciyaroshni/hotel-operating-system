# Generated by Django 2.2 on 2020-10-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainadminapp', '0004_auto_20201003_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logn',
            name='lid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
