from django.urls import path
from .import views

urlpatterns = [
    path('rooms/',views.room_list,name='room_list'),
    path('login/', views.index,name="login"),
]