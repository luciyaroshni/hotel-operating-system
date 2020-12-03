from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
import datetime
from mainadminapp.views import login
from mainadminapp.models import Agent, Floor, Roomcatg, Room, Badmin, Booki, Logn
from django.contrib import messages


def agentdashboard(request):
    usersession = Agent.objects.get(agentid=request.session['agentid'])
    roomavailable = Room.objects.filter(status='available').count
    totalbooking = Room.objects.filter(status='Booked').count
    formatedDate = datetime.date.today()
    checkintoday = Booki.objects.filter(checkin=formatedDate).count()
    checkouttoday = Booki.objects.filter(checkout=formatedDate).count()
    totalguest = Booki.objects.all().count()
    return render(request, 'agdashboard.htmL',
                  {'usersession': usersession, 'countroom': roomavailable, 'checkintoday': checkintoday,
                   'checkouttoday': checkouttoday, 'totalbooking': totalbooking, 'totalguest': totalguest})


def agentbooking(request):
    usersession = Agent.objects.get(agentid=request.session['agentid'])
    abook = Booki.objects.all()
    aagentob = Agent.objects.get(agentid=request.session['agentid'])
    roysuiteval = Roomcatg.objects.filter(catname='ROYAL SUITE')
    presuiteval = Roomcatg.objects.filter(catname='PREMIUM SUITE')
    exesuiteval = Roomcatg.objects.filter(catname='EXECUTIVE SUITE')
    tensuiteval = Roomcatg.objects.filter(catname='TENT CAMPING')

    roomob1 = Room.objects.filter(category=1).filter(status='available')
    roomob2 = Room.objects.filter(category=2).filter(status='available')
    roomob3 = Room.objects.filter(category=3).filter(status='available')
    roomob4 = Room.objects.filter(category=4).filter(status='available')

    now = datetime.date.today()
    if request.method == 'POST' and 'agentsubmit' in request.POST:
        aobjbb = Booki()

        aagentid = Agent.objects.get(agentid=(request.POST.get('aagentid')))
        aguestname = request.POST.get('guestname').title()
        aguestcont = request.POST.get('guestcont')
        aguestemail = request.POST.get('guestemail')
        aguestage = request.POST.get('guestage')
        aguestcountry = request.POST.get('guestcountry').upper()
        aguestcity = request.POST.get('guestcity').upper()
        aguestcheckin = request.POST.get('checkin')
        print(aguestcheckin)
        aaguestcheckout = request.POST.get('checout')
        v200 = request.POST.get('selectedrooms')
        vvv = v200.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        v20 = str2

        aobjbb.agentid = aagentid
        aobjbb.fullname = aguestname
        aobjbb.contactno = aguestcont
        aobjbb.emailg = aguestemail
        aobjbb.age = aguestage
        aobjbb.country = aguestcountry
        aobjbb.city = aguestcity
        aobjbb.roomid = v20
        aobjbb.checkin = aguestcheckin
        aobjbb.checkout = aaguestcheckout
        try:
            aobjbb.save()
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
    return render(request, 'agentbooking.html', {'usersession': usersession, 'abook': abook, 'aagentob': aagentob, 'roomob4': roomob4,'roomob3':roomob3,'roomob1':roomob1,'roomob2':roomob2, 'roysuiteval': roysuiteval, 'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval})


def agentupdate(request):
    usersession = Agent.objects.get(agentid=request.session['agentid'])
    if request.method == 'POST' and 'updateuragent' in request.POST:
        if request.POST.get('aagentname') and request.POST.get('aagentaddress') and request.POST.get('aacontact') and request.POST.get('aaemail') and request.POST.get('aapassword'):
            agentname = request.POST.get('aagentname')
            agentaddress = request.POST.get('aagentaddress')
            agentcontactno = request.POST.get('aacontact')
            agentemailid = request.POST.get('aaemail')
            agentpass = request.POST.get('aapassword')
            obag = Agent.objects.get(agentid=request.session['agentid'])
            obag.agentname = agentname
            obag.agentaddress = agentaddress
            obag.agentcontactno = agentcontactno
            obag.agentemailid = agentemailid
            obag.agentpass = agentpass
            obag.save()
            messages.success(request, 'Successfully Updated Your Record')
            return redirect('http://127.0.0.1:8000/agent/agentupdate')
    return render(request, 'agentsettings.html', {'usersession': usersession})


def agentbookingdetail(request):
    usersession = Agent.objects.get(agentid=request.session['agentid'])
    abook = Booki.objects.filter(agentid=usersession)
    print(abook)
    return render(request, 'agentbookingdetails.html', {'usersession': usersession, 'abook': abook})


def editabooking(request,bookingid):
    usersession = Agent.objects.get(agentid=request.session['agentid'])
    upabook = Booki.objects.get(bookingid=bookingid)
    aagentob = Agent.objects.get(agentid=request.session['agentid'])
    roysuiteval = Roomcatg.objects.filter(catname='ROYAL SUITE')
    presuiteval = Roomcatg.objects.filter(catname='PREMIUM SUITE')
    exesuiteval = Roomcatg.objects.filter(catname='EXECUTIVE SUITE')
    tensuiteval = Roomcatg.objects.filter(catname='TENT CAMPING')

    roomob1 = Room.objects.filter(category=1).filter(status='available')
    roomob2 = Room.objects.filter(category=2).filter(status='available')
    roomob3 = Room.objects.filter(category=3).filter(status='available')
    roomob4 = Room.objects.filter(category=4).filter(status='available')

    f1 = upabook.checkin
    chekd = f1.strftime("%Y-%m-%d")
    print(chekd)
    f2 = upabook.checkout
    cheko = f2.strftime("%Y-%m-%d")

    if request.method == 'POST' and 'upagentsubmit' in request.POST:

        uaguestname = request.POST.get('guestname').title()
        uagentcont = request.POST.get('guestcont')
        uagentemail = request.POST.get('guestemail')
        uagentage = request.POST.get('guestage')
        uagentcountry = request.POST.get('guestcountry')
        uagentcity = request.POST.get('guestcity')
        upagentroomn = request.POST.get('selectedrooms')
        upagentcheckin = request.POST.get('checkin')
        upagentcheckout = request.POST.get('checout')
        vvv = upagentroomn.split(',')  # string to list split by commas
        vvvv = set(vvv)  # list to set to avoid duplication
        vvvvv = list(vvvv)  # set to lst
        str1 = ','.join(vvvvv)  # list to string to save
        str2 = str1.lstrip(',')  # remove left comma of string
        v20 = str2

        upabook.fullname = uaguestname
        upabook.contactno = uagentcont
        upabook.emailg = uagentemail
        upabook.age = uagentage
        upabook.country = uagentcountry
        upabook.city = uagentcity
        upabook.roomid = v20
        upabook.checkin = upagentcheckin
        upabook.checkout = upagentcheckout
        upabook.save()
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
        return redirect('agentbookingdetail')
    return render(request,'editagentbooking.html', context={'cheko':cheko, 'chekd':chekd,'aagentob':aagentob,'usersession': usersession, 'upabook': upabook, 'roomob4': roomob4,'roomob3':roomob3,'roomob1':roomob1,'roomob2':roomob2, 'roysuiteval': roysuiteval, 'presuitval': presuiteval, 'exesuitval': exesuiteval, 'tensuiteval': tensuiteval})


def delabook(request,bookingid):
    delbook = Booki.objects.get(bookingid=bookingid)
    delbook.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/agent/agentbookingdetail')


def aalogout(request):
    request.session['agentid'] = {}
    messages.success(request,"Logged out")
    return redirect(login)