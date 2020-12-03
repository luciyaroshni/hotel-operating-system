from django.contrib import admin
from django.urls import path
from mainadminapp import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),

    path('floor', views.floor, name='floor'),
    path('floor/<int:id>', views.floordelete, name='floordelete'),
    path('editfloor/<int:id>', views.flooredit, name='flooredit'),

    path('aagent', views.agent, name='aagent'),
    path('aagent/<str:agentid>', views.agentdelete, name='aagentdelete'),
    path('editaagent/<str:agentid>', views.agentedit, name='aagentedit'),

    path('badmin', views.badmin, name='badmin'),
    path('badmin/<str:badminid>', views.badmindelete, name='badmindelete'),
    path('editadmin/<str:badminid>', views.badminupdate, name='badminupdate'),

    path('roomcategory', views.roomcategory, name='roomcategory'),
    path('editroomcat/<int:catid>', views.roomcatupdate, name='roomcatupdate'),
    path('roomcategory/<int:catid>', views.roomcatdelete, name='roomcatdelete'),

    path('room', views.room, name='room'),
    path('room/<int:roomid>', views.delroom, name='delroom'),
    path('editroom/<int:roomid>', views.editroom, name='editroom'),

    path('booking', views.booking, name='booking'),
    path('editbooking/<int:bookingid>', views.editbooking, name='editbooking'),
    path('booking/<int:bookingid>', views.delbooking, name='booking'),
    path('editbooking/reciept/<int:bookingid>', views.receipt, name="reciept"),

    path('settings', views.bookingavail, name="settings"),
    path('settings/<int:roomid>', views.makeavail, name="settings"),

    path('setting', views.adminpassword, name="setting"),

    path('guest', views.guest, name="guest"),
    path('alogout', views.alogout, name="alogout"),


]