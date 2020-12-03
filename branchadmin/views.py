from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from mainadminapp.views import login
import datetime
from mainadminapp.models import Agent, Floor, Roomcatg, Room, Badmin, Booki


def bagent(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    showbagent = Agent.objects.all()
    if request.method == 'POST' and 'bagentadd' in request.POST:
        if request.POST.get('bagentname') and request.POST.get('bagentaddress') and request.POST.get(
                    'bagentcontact') and request.POST.get('bagentemail'):
            bagentobj = Agent()
            bagentobj.agentname = request.POST.get('bagentname').title()
            bagentobj.agentaddress = request.POST.get('bagentaddress')
            bagentobj.agentcontactno = request.POST.get('bagentcontact')
            bagentobj.agentemailid = request.POST.get('bagentemail')
            try:
                bagentobj.save()
            except IntegrityError:
                messages.error(request, 'The ' + bagentobj.agentcontactno + ' is already exist')
            else:
                messages.success(request, "Successfully Added " + bagentobj.agentname + " 's Record")
        else:
            messages.error(request, 'Error while adding the record')
    return render(request, 'bagent.html', {'bagentdata': showbagent, 'usersession': usersession})


def bagentdelete(request, agentid):
    delbagent = Agent.objects.get(agentid=agentid)
    delbagent.delete()
    messages.success(request, "Deleted " + delbagent.agentname + "'s Record")
    return redirect('/branchadmin/bagent')


def bagentedit(request, agentid):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    bagu = Agent.objects.get(agentid=agentid)
    if request.method == 'POST' and 'updatebag' in request.POST:
        obbag = Agent.objects.get(agentid=request.POST.get('updatebag'))
        obbag.agentname = request.POST.get('updatebagname').title()
        obbag.agentaddress = request.POST.get('updatebagaddress')
        obbag.agentcontactno = request.POST.get('updatebagcontact')
        obbag.agentemailid = request.POST.get('updatebagemail')

        obbag.save()
        messages.success(request, "Successfully Updated " + obbag.agentname + "'s Record")
        return redirect('/branchadmin/bagent')
    else:
        return render(request, 'editbagent.html', {'bagentdata': bagu, 'usersession': usersession})


def brooms(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    roomobj1 = Floor.objects.all()
    roomobj2 = Roomcatg.objects.all()
    roomobj = Room.objects.all()
    if request.method == 'POST' and 'broomadd' in request.POST:
        if request.POST.get('floord') and request.POST.get('catd'):
            roomob = Room()
            roomob.roomid = request.POST.get('roomno')
            category_obj = Roomcatg.objects.get(catid=int(request.POST.get('catd')))
            roomob.category = category_obj
            room_obj = Floor.objects.get(id=int(request.POST.get('floord')))
            roomob.roomfloor = room_obj
            try:
                roomob.save()
            except IntegrityError:
                messages.error(request, 'The ' + roomob.roomid + ' is Already Exist')
            else:
                messages.success(request, 'Successfully Added ' + roomob.roomid)
        else:
            messages.error(request, 'Error while Adding')
    return render(request, 'brooms.html', {'usersession': usersession,'roome': roomobj2, 'room': roomobj1, 'roomobj': roomobj})


def editbroom(request,roomid):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    uproom = Room.objects.get(roomid=roomid)
    floorobj = Floor.objects.all()
    catobj = Roomcatg.objects.all()
    if request.method == 'POST' and 'updateroomdt' in request.POST:
        if request.POST.get('updateroomfloor') and request.POST.get('updateroomcategory'):
            roomcat = Roomcatg.objects.get(catid=int(request.POST.get('updateroomcategory')))
            roomfloor = Floor.objects.get(id=int(request.POST.get('updateroomfloor')))
            obj = Room.objects.get(roomid=request.POST.get('updateroomdt'))
            obj.category = roomcat
            obj.roomfloor = roomfloor
            obj.save()
            messages.success(request, "Successfully Updated Your Record")
            return redirect('/branchadmin/broom')
    return render(request, 'editbroom.html', {'usersession': usersession, 'uroom': uproom, 'floorobj': floorobj, 'catobj': catobj})


def broomdelete(request, roomid):
    delbroom= Room.objects.get(roomid=roomid)
    delbroom.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/branchadmin/broom')


def bindex(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    roomavailable = Room.objects.filter(status='available').count
    totalbooking = Room.objects.filter(status='Booked').count
    formatedDate = datetime.date.today()
    checkintoday = Booki.objects.filter(checkin=formatedDate).count()
    checkouttoday = Booki.objects.filter(checkout=formatedDate).count()
    totalguest = Booki.objects.all().count()
    return render(request, 'badashboard.html',
                  {'usersession': usersession, 'countroom': roomavailable, 'checkintoday': checkintoday,
                   'checkouttoday': checkouttoday, 'totalbooking': totalbooking, 'totalguest': totalguest})


def bguest(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    guestbad = Booki.objects.all()
    return render(request, 'bguest.html', {'guestbad': guestbad, 'usersession': usersession})


def badroomavail(request,roomid):
    roomav = Room.objects.get(roomid=roomid)
    roomav.status = 'available'
    try:
        roomav.save()
    except Exception:
        messages.error(request, " Error while Adding ")
    else:
        messages.success(request, "Availability Confirmed")
    return redirect('/branchadmin/bsettings')


def badbookingavail(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    roomob = Room.objects.filter(status='Booked')
    return render(request, 'bsett.html', {'usersession': usersession, 'roomob': roomob})


def badminprofile(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    if request.method == 'POST' and 'badminprofile' in request.POST:
        badminname = request.POST.get('badminname')
        badminaddress = request.POST.get('badminaddress')
        badmincontactno = request.POST.get('badmincontact')
        badminemailid = request.POST.get('badminemail')
        badminpass = request.POST.get('badminpass')
        print(badminpass)
        obbd = Badmin.objects.get(badminid=request.session['badminid'])
        obbd.badminname = badminname
        obbd.badminaddress = badminaddress
        obbd.badmincontactno = badmincontactno
        obbd.badminemail = badminemailid
        obbd.badminpass = badminpass
        obbd.save()
        messages.success(request, 'Successfully Updated Your Record')
        return redirect('bindex')
    return render(request, 'updateprofile.html', {'usersession': usersession})


def bbooking(request):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    bbook = Booki.objects.all()
    agentob = Agent.objects.all()
    roysuiteval = Roomcatg.objects.filter(catname='ROYAL SUITE')
    presuiteval = Roomcatg.objects.filter(catname='PREMIUM SUITE')
    exesuiteval = Roomcatg.objects.filter(catname='EXECUTIVE SUITE')
    tensuiteval = Roomcatg.objects.filter(catname='TENT CAMPING')

    roomob1 = Room.objects.filter(category=1).filter(status='available')
    roomob2 = Room.objects.filter(category=2).filter(status='available')
    roomob3 = Room.objects.filter(category=3).filter(status='available')
    roomob4 = Room.objects.filter(category=4).filter(status='available')

    now = datetime.date.today()
    formatedate = now.strftime("%Y %B, %d")

    if request.method == 'POST' and 'searchbag' in request.POST:
        agentob = Agent.objects.all()
        agc = Agent.objects.filter(agentid=request.POST.get('agid'))
        return render(request, 'bbooking.html', context={'usersession': usersession,'roomob4':roomob4,'roomob3':roomob3,'roomob1':roomob1,'roomob2':roomob2,'agc': agc, 'agentob': agentob, 'roysuiteval': roysuiteval, 'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval })
    if request.method == 'POST' and 'bookingsubmit' in request.POST:
        objbb = Booki()
        bguestname = request.POST.get('bfname').title()
        bguestcontactno = request.POST.get('bcont')
        bguestemail = request.POST.get('bemailid')
        bguestage = request.POST.get('bage')
        bguestgen = request.POST.get('bgender')
        bguestmar = request.POST.get('bmard')
        bguestaddress = request.POST.get('baddress')
        bgcountry = request.POST.get('bcountry')
        bgcity = request.POST.get('bcity')
        bgpin = request.POST.get('bpincode', default=000000)
        bguestagent = Agent.objects.get(agentid=(request.POST.get('agid1')))
        bguestnoofrooms = request.POST.get('numberofrooms')
        bguestnoofadults = request.POST.get('numberofadults')
        bguestnoofchild = request.POST.get('numberofchildrens', default=0)
        bguestproof = request.POST.get('proof')
        bguestgrc = request.POST.get('grcno')
        bguestcheckin = request.POST.get('checkin')
        bguestcheckout = request.POST.get('checout')
        bguesttotalamount = request.POST.get('totalamount')
        bguestadvanceamount = request.POST.get('advanceamount')
        bguestbalance = request.POST.get('balanceamount')
        bguestpay = request.POST.get('adamount')
        v200 = request.POST.get('selectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        v20 = str2

        objbb.agentid = bguestagent
        objbb.fullname = bguestname
        objbb.contactno = bguestcontactno
        objbb.emailg = bguestemail
        objbb.age = bguestage
        objbb.gender = bguestgen
        objbb.marital = bguestmar
        objbb.address = bguestaddress
        objbb.country = bgcountry
        objbb.city = bgcity
        objbb.pincode = bgpin
        objbb.noofrooms = bguestnoofrooms
        objbb.roomid = v20
        objbb.noofadults = bguestnoofadults
        objbb.noofchild = bguestnoofchild
        objbb.proof = bguestproof
        objbb.grc = bguestgrc
        objbb.checkin = bguestcheckin
        objbb.checkout = bguestcheckout
        objbb.totalamount = bguesttotalamount
        objbb.adamount = bguestadvanceamount
        objbb.balanceamount = bguestbalance
        objbb.payementmode = bguestpay
        try:
            objbb.save()
        except Exception:
            messages.error(request, " Error while Adding ")
        else:
            messages.success(request, "Booking Successfull")

        roomval = Booki.objects.last().roomid
        print(roomval)
        tolist = roomval.split(',')
        for i in tolist:
            if i != '':
                print(tolist.index(i), i)
                v = Room.objects.get(roomid=i)
                v.status = 'Booked'
                v.save()
                print(v)

        return redirect('bbooking')
    return render(request, 'bbooking.html', {'bbook': bbook,'usersession': usersession, 'agentob': agentob, 'roysuiteval': roysuiteval, 'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval})


def editbbooking(request,bookingid):
    usersession = Badmin.objects.get(badminid=request.session['badminid'])
    upbbook = Booki.objects.get(bookingid=bookingid)
    bagentob = Agent.objects.all()
    roysuiteval = Roomcatg.objects.filter(catname='ROYAL SUITE')
    presuiteval = Roomcatg.objects.filter(catname='PREMIUM SUITE')
    exesuiteval = Roomcatg.objects.filter(catname='EXECUTIVE SUITE')
    tensuiteval = Roomcatg.objects.filter(catname='TENT CAMPING')

    roomob1 = Room.objects.filter(category=1).filter(status='available')
    roomob2 = Room.objects.filter(category=2).filter(status='available')
    roomob3 = Room.objects.filter(category=3).filter(status='available')
    roomob4 = Room.objects.filter(category=4).filter(status='available')

    formatda = upbbook.checkin
    chekd = formatda.strftime("%Y-%m-%d")
    formatda1 = upbbook.checkout
    cheko = formatda1.strftime("%Y-%m-%d")

    if request.method == 'POST' and 'searchbag' in request.POST:
        bagentob = Agent.objects.all()
        agc = Agent.objects.filter(agentid=request.POST.get('uagid'))
        return render(request, 'editbbooking.html', context={ 'cheko' :cheko, 'chekd': chekd,'upbbook': upbbook, 'agentob': bagentob,'usersession': usersession,'roomob4':roomob4,'roomob3':roomob3,'roomob1':roomob1,'roomob2':roomob2,'agc': agc, 'roysuiteval': roysuiteval, 'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval })
    if request.method == 'POST' and 'updatebbook' in request.POST:
        buguestagent = Agent.objects.get(agentid=(request.POST.get('uagid1')))
        uobjbb = Booki.objects.get(bookingid=bookingid)
        bfullname = request.POST.get('ubfname').title()
        print(bfullname)
        print('hi')
        bcontact = request.POST.get('ubcont')
        bemail = request.POST.get('ubemailid')
        bage = request.POST.get('ubbage')
        bgender = request.POST.get('upbgender')
        bmarital = request.POST.get('ubdatemarital')
        baddress = request.POST.get('ubbaddress')
        bcity = request.POST.get('ubbcity').upper()
        bcountry = request.POST.get('ubcountry').upper()
        bpincode = request.POST.get('ubpincode')
        bnoofroom = request.POST.get('numberofrooms')
        bnoofadults = request.POST.get('unumberofadults')
        bnoofchild = request.POST.get('unumberofchildrens')
        bproofsub = request.POST.get('uproof')
        bgrc = request.POST.get('ugrcno')
        bcheckin = request.POST.get('ucheckin')
        bcheckout = request.POST.get('uchecout')
        btotal = request.POST.get('totalamount')
        badvanceamount = request.POST.get('advanceamount')
        bbalance = request.POST.get('balanceamount')
        paymentmode = request.POST.get('paymentmode')
        v200 = request.POST.get('selectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        v20 = str2

        uobjbb.agentid = buguestagent
        uobjbb.fullname = bfullname
        uobjbb.contactno = bcontact
        uobjbb.emailg = bemail
        uobjbb.age = bage
        uobjbb.gender = bgender
        uobjbb.marital = bmarital
        uobjbb.address = baddress
        uobjbb.country = bcountry
        uobjbb.city = bcity
        uobjbb.pincode = bpincode
        uobjbb.noofrooms = bnoofroom
        uobjbb.roomid = v20
        uobjbb.noofadults = bnoofadults
        uobjbb.noofchild = bnoofchild
        uobjbb.proof = bproofsub
        uobjbb.grc = bgrc
        uobjbb.checkin = bcheckin
        uobjbb.checkout = bcheckout
        uobjbb.totalamount = btotal
        uobjbb.adamount = badvanceamount
        uobjbb.balanceamount = bbalance
        uobjbb.payementmode = paymentmode
        uobjbb.save()
        roomval = Booki.objects.last().roomid
        print(roomval)
        tolist = roomval.split(',')
        for i in tolist:
            if i != '':
                print(tolist.index(i), i)
                v = Room.objects.get(roomid=i)
                v.status = 'Booked'
                v.save()
                print(v)
        return redirect('breciept',bookingid=bookingid)
    return render(request,'editbbooking.html',context={'cheko': cheko, 'chekd': chekd,'upbbook':upbbook,'agentob': bagentob})


def blogout(request):
    request.session['badminid'] = {}
    messages.success(request,"Logged out")
    return redirect(login)


def breciept(request,bookingid):
    recbook = Booki.objects.get(bookingid=bookingid)
    return render(request,"breciept.html",{'recbook': recbook})