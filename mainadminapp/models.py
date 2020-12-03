
from django.db import models

# Create your models here.


def agent_id_increment():
    last_invoice = Agent.objects.all().last()
    if not last_invoice:
        return 'ARG0001'
    agentid = last_invoice.agentid
    new_invoice_no = str(int(agentid[4:]) + 1)
    new_invoice_no = agentid[0:-(len(new_invoice_no))] + new_invoice_no
    return new_invoice_no


def admin_id_increment():
    last_in = Badmin.objects.all().last()
    if not last_in:
        return 'ARA0001'
    badminid = last_in.badminid
    new_in = str(int(badminid[4:]) + 1)
    new_in = badminid[0:-(len(new_in))] + new_in
    return new_in


class Floor(models.Model):
    floorno = models.CharField(unique=True, max_length=20)
    noofrooms = models.IntegerField()


class Agent(models.Model):
    agentid = models.CharField(primary_key=True, max_length=10, default=agent_id_increment)
    agentname = models.CharField(max_length=25)
    agentaddress = models.CharField(max_length=70)
    agentcontactno = models.CharField(max_length=10)
    agentemailid = models.EmailField(max_length=30)
    agentpass = models.CharField(max_length=30, default=123)
    agentvalue = models.IntegerField(default=4)


class Badmin(models.Model):
    badminid = models.CharField(primary_key=True, max_length=10, default=admin_id_increment)
    badminname = models.CharField(max_length=25)
    badminaddress = models.CharField(max_length=70)
    badmincontactno = models.CharField(max_length=10)
    badminemail = models.EmailField(max_length=30)
    badminpass = models.CharField(max_length=30, default=345)
    badminvalue = models.IntegerField(default=3)


class Roomcatg(models.Model):
    catid = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=25, unique=True)
    catarea = models.CharField(max_length=20)
    catfood = models.CharField(max_length=10)
    catbev = models.CharField(max_length=10)
    catwifi = models.CharField(max_length=10)
    catac = models.CharField(max_length=10)
    catrate = models.CharField(max_length=10)


class Room(models.Model):
    roomid = models.IntegerField(primary_key=True, unique=True)
    category = models.ForeignKey(Roomcatg, db_column='category', on_delete=models.CASCADE)
    roomfloor = models.ForeignKey(Floor, db_column='roomfloor', on_delete=models.CASCADE)
    status = models.CharField(max_length=20,default='available')


class Logn(models.Model):
    lid = models.CharField(primary_key=True, max_length=20)
    luname = models.CharField(max_length=25)
    lpass = models.CharField(max_length=25)
    key_value = models.IntegerField(default=5)


class Count(models.Model):
    coid = models.AutoField(primary_key=True, unique=True)
    coname = models.CharField(max_length=30)


class City(models.Model):
    citid = models.AutoField(primary_key=True, unique=True)
    ctname = models.CharField(max_length=30)
    coid = models.ForeignKey(Count, db_column='coid', on_delete=models.CASCADE)


class Booki(models.Model):
    bookingid = models.AutoField(primary_key=True, unique=True)
    agentid = models.ForeignKey(Agent, db_column='agentid',on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    contactno = models.CharField(max_length=10)
    emailg = models.EmailField(max_length=25)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=20)
    marital = models.CharField(max_length=15)
    address = models.CharField(max_length=70, default=0)
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    pincode = models.CharField(max_length=6, default=0)
    noofrooms = models.IntegerField(default=0)
    roomid = models.CharField(max_length=200)
    noofadults = models.IntegerField(default=0)
    noofchild = models.IntegerField(default=0)
    proof = models.CharField(max_length=30)
    grc = models.CharField(max_length=30)
    checkin = models.DateField()
    checkout = models.DateField()
    totalamount = models.CharField(max_length=50,default=0)
    adamount = models.CharField(max_length=30,default=0)
    balanceamount = models.CharField(max_length=30,default=0)
    payementmode = models.CharField(max_length=30,default=0)
