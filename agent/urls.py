from django.urls import path
from agent import views


urlpatterns = [

    path('agentdashboard', views.agentdashboard, name="agentdashboard"),
    path('agentbooking', views.agentbooking, name="agentbooking"),
    path('agentupdate', views.agentupdate, name="agentupdate"),
    path('agentbookingdetail', views.agentbookingdetail, name="agentbookingdetail"),
    path('editabooking/<int:bookingid>', views.editabooking, name='editabooking'),
    path('agentbookingdetail/<int:bookingid>', views.delabook, name= 'agentbookingdetail'),
    path('aalogout', views.aalogout, name="aalogout"),
]
