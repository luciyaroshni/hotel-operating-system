# Generated by Django 2.2 on 2020-10-23 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainadminapp', '0006_auto_20201021_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booki',
            name='agentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.Agent'),
        ),
    ]
