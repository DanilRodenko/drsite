from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from app1.models import Player, Trading_Pairs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re


import pandas as pd

# Create your views here.
# test view
def users_login(request):
    n = []
    for x in User.objects.all():
        n.append(x)
        n.append(' ')
    return HttpResponse(n)


def trading_pairs(request):
    n = []
    for pair in Trading_Pairs.objects.all():
        n.append(pair.buy)
        n.append(pair.sell)
    return  HttpResponse(n)
#Main_Page
def main_page(request):
    context = {

    }
    return render(
        request,
        'main_menu.html',
        context
    )


def login_user(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is None:
        return render(request, 'error_login.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('main_page')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('main_page')
    else:
        return HttpResponseRedirect('main_page')

def registration(request):
    return render(
        request,
        'registration.html'
    )

def register(request):
    if len(request.POST['login']) < 3 or len(request.POST['password']) < 4:
        return HttpResponseRedirect('reg')
    elif request.POST['login'] in User.objects.all():
        return HttpResponseRedirect('reg')
    else:
        user = User.objects.create_user(
            request.POST['login'],
            password=request.POST['password'],
            email= request.POST['email'],
            first_name=request.POST['first_name']
        )
        user.save()
        return HttpResponseRedirect('main_page')


def ajax_path(request):
    response = {
        'number' : 1710
    }
    return JsonResponse(response)

def check_login(request):
    name = request.POST['login']
    if len(User.objects.filter(username=name)) == 0:
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})

def check_mail(request):
    email = request.POST['email']
    if len(User.objects.filter(email=email)) == 0:
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})



def register_with_ajax(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        email=request.POST['email'],
        first_name=request.POST['first_name']
    )
    return JsonResponse({'status': 'ok'})

def news_page(request):
    return render(
        request,
        'news.html'
    )