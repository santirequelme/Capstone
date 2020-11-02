import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import random
from .models import User, Hiking, Comment, Booking, Favourite
from .forms import booking_form
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.views.decorators.http import require_http_methods

def index(request):
    hikings = Hiking.objects.all()
    if hikings is None:
        return render(request, "hiking/index.html",{
        "active":False
    })
    return render(request, "hiking/index.html",{
        "active":hikings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

  
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hiking/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "hiking/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hiking/register.html", {
                "message": "Passwords must match."
            })

    
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "hiking/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hiking/register.html")

def api(request):
    bookings = Booking.objects.filter(user=request.user)
    bookings = bookings.order_by("-timestamp").all()
    return JsonResponse([booking.serialize() for booking in bookings], safe=False)

@login_required(login_url='/')
def profile(request):
    bookings = Booking.objects.all()
    return render(request, "hiking/profile.html", {
        'bookings':bookings})

@login_required(login_url='/')
def filterby(request):
    if request.method == "GET":
        return render(request, "hiking/filterby.html")
    else:
        location = request.POST["location"]
        level = request.POST["level"]
        if (location=="all" and level == "any"):
            hikings= Hiking.objects.all()
        elif (location == "all"):
            hikings= Hiking.objects.filter(level=level)
        elif (level == "any"):
            hikings= Hiking.objects.filter(location=location)
        else:
            hikings= Hiking.objects.filter(location=location, level=level)
        if len(hikings)>0:
            boolean = True
        else:
            boolean = False
        return render(request, "hiking/filterby.html", {
            "active": hikings, 
            "boolean": boolean
            })

@login_required(login_url="/")
def singlehike(request, id):
    hiking = Hiking.objects.get(id=id)
    userfavourite = Favourite.objects.filter(user=request.user).values('hiking_id')

    favourite = []
    for content in userfavourite:
        favourite.append(content['hiking_id'])
    if id in favourite:
        boolean = True
    else:
        boolean = False

    comments = Comment.objects.filter(hiking=hiking).values('id')
    comment_list = []
    for content in comments:
        comment = Comment.objects.get(id=content['id'])
        comment_list.append(comment)
    form = booking_form()
    return render(request, "hiking/singlehike.html", {
            "hiking": hiking,
            "comments":comment_list,
            "favourite":boolean,
            "form":form
            })

@login_required(login_url='/')
def favourite(request):
    user = request.user
    hikings =Favourite.objects.filter(user=user).values('hiking_id')
    favourite= []
    for hiking in hikings:
            favo = Hiking.objects.get(id = hiking['hiking_id'])
            favourite.append(favo)
    if favourite is None:
        return render(request, "hiking/favourite.html", {
            "favourite":False
        })
    return render(request, "hiking/favourite.html",{
        "favourite": favourite
    })

@login_required(login_url='/')
def favswitcher(request,id):
    user = request.user
    hiking = Hiking.objects.get(id=id)
    if Favourite.objects.filter(user=user, hiking=hiking).exists():
        favo = Favourite.objects.get(user=user,hiking=hiking)
        favo.delete()
        return HttpResponseRedirect(reverse("singlehike", args=(),
            kwargs={'id': id}))
    else:
        favo = Favourite(user=user, hiking=hiking)
        favo.save()
        return HttpResponseRedirect(reverse("singlehike", args=(),
            kwargs={'id': id}))

    
@login_required(login_url='/')
def booking(request):
    if request.method == "POST":
        form = booking_form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.book_number = random.randrange(10000, 99999)
            booking.hike = request.POST["hike"]
            booking.save()
        return HttpResponseRedirect(reverse("profile"))
    else:
        form = booking_form()
        return render (request, "hiking/singlehike.html",
         {'form':form
          })

@login_required(login_url='/')
def comment(request, id):

    user= request.user
    hiking= Hiking.objects.get(id =id)
    if request.method == "POST":
        comment = request.POST.get("comment")
        new_comment= Comment (user = user, hiking =hiking, comment=comment)
        new_comment.save()

    return HttpResponseRedirect(reverse("singlehike", args=(), kwargs={'id':id}))




