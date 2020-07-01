from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse
import re, random, sys, os
import pdfkit
# from .models import Profile, Story, Region #적용할 모델들


def home(request):
    return render(request, 'intro.html')

def aboutPage(request):
    return render(request, 'about.html')

def functionPage(request):
    return render(request, 'function.html')

def streamingPage(request):
    return render(request, 'streaming.html')

def cornellPage(request):
    return render(request, 'cornell.html')

def cnDetail(request):
    return render(request, 'cornellDetail.html')

def resultPage(request):
    return render(request, 'result.html')

def creditPage(request):
    return render(request, 'credit.html')