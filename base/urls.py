from django.contrib import admin
from django.urls import path, include
from base import views
urlpatterns = [
    path('', views.home,name="home"),
    path('room/<str:pk>', views.room,name="room"),
    path('create_room/', views.create_rooms,name="create_rooms"),
    path('update_room/<int:pk>', views.update_rooms,name="update_rooms"),
    path('delete_room/<int:pk>', views.delete_rooms,name="delete_rooms"),
    path('delete_message/<int:pk>', views.delete_message,name="delete_message"),
    path('delete_topic/<int:pk>', views.delete_topic,name="delete_topic"),

   
     
    
    
]
