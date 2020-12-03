import datetime

from django.http import HttpResponse

from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import IntegrityError, DataError
from django.contrib import messages
from mainadminapp.models import Floor, Agent, Badmin, Roomcatg, Room, Logn, Count, City, Booki


def index(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    roomavailable = Room.objects.filter(status='available').count
    totalbooking = Room.objects.filter(status='Booked').count
    formatedDate = datetime.date.today()
    checkintoday = Booki.objects.filter(checkin=formatedDate).count()
    checkouttoday = Booki.objects.filter(checkout=formatedDate).count()
    totalguest = Booki.objects.all().count()
    return render(request, 'adashboard.html', {'usersession': usersession, 'countroom': roomavailable, 'checkintoday': checkintoday, 'checkouttoday': checkouttoday, 'totalbooking': totalbooking, 'totalguest': totalguest})


def floor(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    showall = Floor.objects.all()
    if request.method == 'POST' and 'flooradd' in request.POST:
        if request.POST.get('floorno') and request.POST.get('noofrooms'):
            floors = Floor()
            floors.floorno = request.POST.get('floorno').title()

            floors.noofrooms = request.POST.get('noofrooms')
            try:
                floors.save()
            except IntegrityError:
                messages.error(request, 'The '+floors.floorno+' is already exist')
            else:
                messages.success(request, 'Successfully Added '+floors.floorno)
        else:
            messages.error(request, 'Error while adding the record')
    return render(request, 'floor.html', {'data': showall, 'usersession': usersession})


def floordelete(request, id):
    delfloor = Floor.objects.get(id=id)
    delfloor.delete()
    return redirect('/mainadminapp/floor')


def flooredit(request,id):
    usersession = Logn.objects.get(lid=request.session['lid'])
    upf = Floor.objects.get(id=id)
    if request.method == 'POST' and 'updatefloor' in request.POST:
        floorno = request.POST.get('updatefloorno').title()
        noofrooms = request.POST.get('updateroom')
        ob = Floor.objects.get(id=request.POST.get('updatefloor'))
        ob.floorno = floorno
        ob.noofrooms = noofrooms
        try:
            ob.save()
        except IntegrityError:
            messages.error(request, 'Sorry The ' + ob.floorno + ' is Already Exist.')
        else:
            messages.success(request, "Successfully Updated Your Record")
        return redirect("/mainadminapp/floor")
    else:
        return render(request, 'editfloor.html', {'data': upf, 'usersession': usersession})


def agent(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    showagent = Agent.objects.all()
    if request.method == 'POST' and 'agentadd' in request.POST:
        if request.POST.get('agentname') and request.POST.get('agentaddress') and request.POST.get('agentcontact') and request.POST.get('agentemail'):
            agentobj = Agent()
            agentobj.agentname = request.POST.get('agentname').title()
            agentobj.agentaddress = request.POST.get('agentaddress')
            agentobj.agentcontactno = request.POST.get('agentcontact')
            agentobj.agentemailid = request.POST.get('agentemail')
            try:
                agentobj.save()
            except IntegrityError:
                messages.error(request, 'The ' + agentobj.agentcontactno + ' is already exist')
            else:
                messages.success(request, 'Successfully Added')
        else:
            messages.error(request, 'Error while adding the record')
    return render(request, 'agent.html', {'agentdata':showagent, 'usersession': usersession})


def agentdelete(request, agentid):
    delagent = Agent.objects.get(agentid=agentid)
    delagent.delete()
    messages.success(request, "Deleted " + delagent.agentname + "'s Record")
    return redirect('/mainadminapp/agent')


def agentedit(request, agentid):
    usersession = Logn.objects.get(lid=request.session['lid'])
    agu = Agent.objects.get(agentid=agentid)
    if request.method == 'POST' and 'updateagent' in request.POST:
        agentname = request.POST.get('updateagentname')
        agentaddress = request.POST.get('updateagentaddress')
        agentcontactno = request.POST.get('updateagentcontact')
        agentemailid = request.POST.get('updateagentemail')
        obag = Agent.objects.get(agentid=request.POST.get('updateagent'))
        obag.agentname = agentname
        obag.agentaddress = agentaddress
        obag.agentcontactno = agentcontactno
        obag.agentemailid = agentemailid
        obag.save()
        messages.success(request, "Successfully Updated " + obag.agentname + "'s Record")
        return redirect("/mainadminapp/agent")
    else:
        return render(request, 'editagent.html', {'agentdata': agu, 'usersession': usersession})


def badmin(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    addadmin = Badmin.objects.all()
    if request.method == 'POST' and 'addadmin' in request.POST:
        if request.POST.get('adminname') and request.POST.get('adminaddress') and request.POST.get('admincontact') and request.POST.get('adminemail'):
            badobj = Badmin()
            badobj.badminname = request.POST.get('adminname')
            badobj.badminaddress = request.POST.get('adminaddress')
            badobj.badmincontactno = request.POST.get('admincontact')
            badobj.badminemail = request.POST.get('adminemail')
            badobj.save()
            messages.success(request, "Successfully Added " + badobj.badminname + "'s Record")
        else:
            messages.error(request, 'Error while adding the record')

    return render(request, 'badmin.html', {'showadmin': addadmin, 'usersession': usersession})


def badmindelete(request, badminid):
    delbadmin = Badmin.objects.get(badminid=badminid)
    delbadmin.delete()
    messages.success(request, "Deleted " + delbadmin.badminname + "'s Record")
    return redirect('/mainadminapp/badmin')


def badminupdate(request, badminid):
    usersession = Logn.objects.get(lid=request.session['lid'])
    upba = Badmin.objects.get(badminid=badminid)
    if request.method == 'POST' and 'updateadmin' in request.POST:
        badminname = request.POST.get('updatebadminname')
        badminaddress = request.POST.get('updatebadminaddress')
        badmincontactno = request.POST.get('updatebadmincontactno')
        badminemail = request.POST.get('updatebadminemail')
        objba = Badmin.objects.get(badminid=request.POST.get('updateadmin'))
        objba.badminname = badminname
        objba.badminaddress = badminaddress
        objba.abadmincontactno = badmincontactno
        objba.badminemail = badminemail
        objba.save()
        messages.success(request, "Successfully Updated " + objba.badminname + "'s Record")
        return redirect("/mainadminapp/badmin")
    else:
        return render(request, 'editadmin.html', {'showadmin': upba,'usersession': usersession})


def roomcategory(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    cat = Roomcatg.objects.all()
    if request.method == 'POST' and 'catadd' in request.POST:
        if request.POST.get('catname') and request.POST.get('roomarea') and request.POST.get('food') and request.POST.get('bev') and request.POST.get('wifi') and request.POST.get('ac') and request.POST.get('rater') :
            roomcat = Roomcatg()
            roomcat.catname = request.POST.get('catname')
            roomcat.catarea = request.POST.get('roomarea')
            roomcat.catfood = request.POST.get('food')
            roomcat.catbev = request.POST.get('bev')
            roomcat.catwifi = request.POST.get('wifi')
            roomcat.catac = request.POST.get('ac')
            roomcat.catrate = request.POST.get('rater')
            if Roomcatg.objects.filter(catname = roomcat.catname).exists():
                messages.error(request, 'Already Exist')
                return redirect('http://127.0.0.1:8000/mainadminapp/roomcategory')
            else:
                try:
                    roomcat.save()
                except IntegrityError:
                     messages.error(request, 'The ' + roomcat.catname + ' is already exist')
                else:
                    messages.success(request, 'Successfully Added ' + roomcat.catname)
        else:
            messages.error(request, 'Error while adding the record')
    return render(request, 'roomcategory.html', {'catdata': cat, 'usersession': usersession})


def roomcatupdate(request, catid):
    usersession = Logn.objects.get(lid=request.session['lid'])
    uprcat = Roomcatg.objects.get(catid=catid)
    if request.method == 'POST' and 'updateroomcat' in request.POST:
        catnamee = request.POST.get('updateroomcatname')
        catareaa = request.POST.get('updateroomcatarea')
        catfoodd = request.POST.get('updateroomfood')
        catbevv = request.POST.get('updatebev')
        catwifii = request.POST.get('updatecatwifi')
        catacc = request.POST.get('updatecatac')
        catratee = request.POST.get('updatecatrater')
        objcat = Roomcatg.objects.get(catid=request.POST.get('updateroomcat'))
        objcat.catname = catnamee
        objcat.catarea = catareaa
        objcat.catfood = catfoodd
        objcat.catbev = catbevv
        objcat.catwifi = catwifii
        objcat.catac = catacc
        objcat.catrate = catratee
        try:
            objcat.save()
        except IntegrityError:
            messages.error(request, 'Sorry The ' + objcat.catname + ' is Already Exist.')
        else:
            messages.success(request, "Successfully Updated Your Record")
        return redirect("/mainadminapp/roomcategory")
    else:
        return render(request, 'editroomcat.html', {'showroomcat': uprcat, 'usersession': usersession})


def roomcatdelete(request, catid):
    delroomcat = Roomcatg.objects.get(catid=catid)
    delroomcat.delete()
    messages.success(request, "Deleted " + delroomcat.catname + "'s Record")
    return redirect('/mainadminapp/roomcategory')


def room(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    roomobj1 = Floor.objects.all()
    roomobj2 = Roomcatg.objects.all()
    roomobj = Room.objects.all()
    if request.method == 'POST' and 'roomadd' in request.POST:
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
    return render(request, 'room.html', {'roome': roomobj2, 'room': roomobj1, 'roomobj': roomobj, 'usersession': usersession})


def delroom(request, roomid):
    delrm = Room.objects.get(roomid=roomid)
    delrm.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('/mainadminapp/room')


def editroom(request, roomid):
    usersession = Logn.objects.get(lid=request.session['lid'])
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
            return redirect('/mainadminapp/room')
    return render(request, 'editroom.html', {'usersession':usersession, 'uroom': uproom, 'floorobj': floorobj, 'catobj': catobj})


def booking(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
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
        return render(request, 'booking.html',
                      context={'usersession': usersession, 'roomob4': roomob4, 'roomob3': roomob3, 'roomob1': roomob1,
                               'roomob2': roomob2, 'agc': agc, 'agentob': agentob, 'roysuiteval': roysuiteval,
                               'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval})
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

        return redirect('booking')
    return render(request, 'booking.html',
                  {'bbook': bbook, 'usersession': usersession, 'agentob': agentob, 'roysuiteval': roysuiteval,
                   'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval})


def editbooking(request,bookingid):
    usersession = Logn.objects.get(lid=request.session['lid'])
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
        return render(request, 'editbooking.html',
                      context={'cheko': cheko, 'chekd': chekd, 'upbbook': upbbook, 'agentob': bagentob,
                               'usersession': usersession, 'roomob4': roomob4, 'roomob3': roomob3, 'roomob1': roomob1,
                               'roomob2': roomob2, 'agc': agc, 'roysuiteval': roysuiteval, 'presuitval': presuiteval,
                               'exesuitval': exesuiteval, 'tensuiteval': tensuiteval})
    if request.method == 'POST' and 'updatebbook' in request.POST:
        buguestagent = Agent.objects.get(agentid=(request.POST.get('uagid')))
        uobjbb = Booki.objects.get(bookingid=bookingid)
        bfullname = request.POST.get('ubfname').title()
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
        badamount = request.POST.get('adamount')
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
        uobjbb.payementmode = badamount
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

        return redirect('reciept', bookingid=bookingid)
    return render(request, 'editbooking.html',
                  context={'cheko': cheko, 'chekd': chekd, 'upbbook': upbbook, 'agentob': bagentob})


def delbooking(request,bookingid):
    delbook = Booki.objects.get(bookingid=bookingid)
    delbook.delete()
    messages.success(request,"Deleted "+delbook.fullname+ " 's record")
    return redirect('http://127.0.0.1:8000/mainadminapp/booking')


def login(request):
    if request.method == 'POST' and 'loginb' in request.POST:
        if Logn.objects.filter(lid=request.POST['uname'], lpass=request.POST['password']).exists():
            uname = request.POST.get('uname')
            request.session['lid'] = uname
            Logn.objects.get(lid=uname, lpass=request.POST['password'])
            return redirect('/mainadminapp/index')
        elif Badmin.objects.filter(badminid=request.POST['uname'], badminpass=request.POST['password']).exists():
            uname = request.POST.get('uname')
            request.session['badminid'] = uname
            Badmin.objects.get(badminid=uname, badminpass=request.POST['password'])
            return redirect('branchadmin/bindex')
        elif Agent.objects.filter(agentid = request.POST['uname'], agentpass = request.POST['password']).exists():
            uname = request.POST.get('uname')
            request.session['agentid'] = uname
            Agent.objects.get(agentid = request.POST['uname'], agentpass = request.POST['password'])
            return redirect('agent/agentdashboard')
        else:
            messages.error(request, 'Invalid username or Password')
            return redirect('/login')
    return render(request, 'login.html')


def bookingavail(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    roomob1 = Room.objects.filter(status='Booked')
    return render(request, 'settings.html', {'usersession': usersession, 'roomob1': roomob1})


def makeavail(request,roomid):
    delrm = Room.objects.get(roomid=roomid)
    delrm.status = 'available'
    try:
        delrm.save()
    except Exception:
        messages.error(request, " Error while Adding ")
    else:
        messages.success(request, "Availability Confirmed")
    return redirect('/mainadminapp/settings')


def adminpassword(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    if request.method == 'POST' and 'updateadmin' in request.POST:
        currentusername = request.POST.get('currentusername')
        newusername = request.POST.get('newusername')
        confirmusername = request.POST.get('confirmusername')
        username = Logn.objects.get(lid=request.session['lid'])
        if currentusername == username.lpass:
            if newusername == confirmusername:
                username.lpass = newusername
                username.save()
                messages.success(request,  "Password changed successfully")
                return redirect('index')
            else:
                messages.error(request,'Password mismatch')
                return redirect('setting')
        else:
            messages.error(request,'Enter your current password')
            return redirect('setting')

    return render(request, 'adminchangepass.html', {'usersession': usersession})


def guest(request):
    usersession = Logn.objects.get(lid=request.session['lid'])
    guest1 = Booki.objects.all()
    print(guest1)
    return render(request, 'guest.html', {'guest1': guest1, 'usersession': usersession})


def receipt(request,bookingid):
    recbook = Booki.objects.get(bookingid=bookingid)
    return render(request, "receipt.html", {'recbook': recbook})


def alogout(request):
    request.session['lid'] = {}
    messages.success(request,"Logged out")
    return redirect(login)