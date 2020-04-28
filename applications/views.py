from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse
import re, random
# from .models import Profile, Story, Region #적용할 모델들

def home(request):
    return render(request, 'intro.html')

def streamingPage(request):
    return render(request, 'subject.html')

def preparePage(request):
    return render(request, 'prepare.html')