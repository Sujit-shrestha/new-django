from django.urls import path
from .import views

urlpatterns = [
    path('rooms/',views.room_list,name='room_list'),
    path('home/', views.index,name="home"),
]