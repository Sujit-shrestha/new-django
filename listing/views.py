from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth import authenticate,login,logout
from .models import Room,User
# Create your views here.

def room_list(request):
    rooms = Room.objects.all()
    serialized_rooms = serialize('json', rooms)
    return JsonResponse({"rooms":serialized_rooms}, safe=False)


def index(request):
    if request.user.is_authenticated:
        return JsonResponse({"user":"logged in"})
    return JsonResponse({"login":"login_view"})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username,password=password)

        # check if authentication sucessful
        if user is not None:
            login(request,user)
            return JsonResponse({"user":"login sucessful"})

        else:
            return JsonResponse({"user":"login failed"})


def logout_view(request):
    logout(request)
    return JsonResponse({"user":"logged out"})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # password confirm
        password = request.POST["password"]
        confirm = request.POST["confirmation"]

        if password != confirm:
            return JsonResponse({"user":"password unmatched"})
        
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
        
        except IntegrityError:
            return JsonResponse({"user": "integrity error"})
        
        login(request,user)
        return JsonResponse({"user": "logged in"})
    else:
        return JsonResponse({"user":"register view"})