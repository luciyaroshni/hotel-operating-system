# Generated by Django 2.2 on 2020-09-10 08:21

from django.db import migrations, models
import django.db.models.deletion
import mainadminapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('agentid', models.CharField(default=mainadminapp.models.agent_id_increment, max_length=10, primary_key=True, serialize=False)),
                ('agentname', models.CharField(max_length=25)),
                ('agentaddress', models.CharField(max_length=70)),
                ('agentcontactno', models.CharField(max_length=10)),
                ('agentemailid', models.EmailField(max_length=30)),
                ('agentpass', models.CharField(default=123, max_length=30)),
                ('agentvalue', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Badmin',
            fields=[
                ('badminid', models.CharField(default=mainadminapp.models.admin_id_increment, max_length=10, primary_key=True, serialize=False)),
                ('badminname', models.CharField(max_length=25)),
                ('badminaddress', models.CharField(max_length=70)),
                ('badmincontactno', models.CharField(max_length=10)),
                ('badminemail', models.EmailField(max_length=30)),
                ('badminpass', models.CharField(default=345, max_length=30)),
                ('badminvalue', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('coid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('coname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorno', models.CharField(max_length=20, unique=True)),
                ('noofrooms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Logn',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('luname', models.CharField(max_length=25)),
                ('lpass', models.CharField(max_length=25)),
                ('key_value', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Roomcatg',
            fields=[
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=25, unique=True)),
                ('catarea', models.CharField(max_length=20)),
                ('catfood', models.CharField(max_length=10)),
                ('catbev', models.CharField(max_length=10)),
                ('catwifi', models.CharField(max_length=10)),
                ('catac', models.CharField(max_length=10)),
                ('catrate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(default='available', max_length=20)),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.Roomcatg')),
                ('roomfloor', models.ForeignKey(db_column='roomfloor', on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.Floor')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('citid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ctname', models.CharField(max_length=30)),
                ('coid', models.ForeignKey(db_column='coid', on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.Count')),
            ],
        ),
        migrations.CreateModel(
            name='Booki',
            fields=[
                ('bookingid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fullname', models.CharField(max_length=30)),
                ('contactno', models.CharField(max_length=10)),
                ('emailg', models.EmailField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('marital', models.CharField(max_length=15)),
                ('address', models.CharField(default=None, max_length=70)),
                ('pincode', models.CharField(default=0, max_length=6)),
                ('noofrooms', models.IntegerField()),
                ('roomno', models.CharField(max_length=200)),
                ('noofadults', models.IntegerField()),
                ('noofchild', models.IntegerField(default=0)),
                ('proof', models.CharField(max_length=30)),
                ('grc', models.CharField(max_length=30)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('totalamount', models.CharField(max_length=50)),
                ('adamount', models.CharField(max_length=30)),
                ('balanceamount', models.CharField(max_length=30)),
                ('payementmode', models.CharField(max_length=30)),
                ('agentid', models.ForeignKey(db_column='agentidf', on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.Agent')),
                ('city', models.ForeignKey(db_column='city', on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.City')),
                ('country', models.ForeignKey(db_column='country', on_delete=django.db.models.deletion.CASCADE, to='mainadminapp.Count')),
            ],
        ),
    ]
