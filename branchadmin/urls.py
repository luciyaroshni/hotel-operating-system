from django.urls import path
from branchadmin import views


urlpatterns = [
    path('bagent', views.bagent, name='bagent'),
    path('bagent/<str:agentid>', views.bagentdelete, name='bagentdelete'),
    path('editbagent/<str:agentid>', views.bagentedit, name='bagentedit'),
    path('broom', views.brooms, name='broom'),
    path('editbroom/<int:roomid>', views.editbroom, name='editbroom'),
    path('broom/<int:roomid>', views.broomdelete, name= 'broom'),
    path('bindex', views.bindex, name='bindex'),
    path('bguest', views.bguest, name='bguest'),
    path('bsetting', views.badbookingavail, name="bsetting"),
    path('bsettings/<int:roomid>', views.badroomavail, name="bsettings"),

    path('bsettings', views.badminprofile, name="bsettings"),


    path('bbooking', views.bbooking, name="bbooking"),
    path('blogout', views.blogout, name="blogout"),
    path('editbbooking/<int:bookingid>', views.editbbooking, name= "editbbooking"),
    path('editbbooking/breciept/<int:bookingid>', views.breciept, name = "breciept"),
]