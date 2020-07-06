from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Mynote
import re, random


def home(request):
    return render(request, 'intro.html')

def aboutPage(request):
    return render(request, 'about.html')

def functionPage(request):
    return render(request, 'function.html')

def streamingPage(request):
    return render(request, 'streaming.html')

def cornellPage(request):
    mynotes = Mynote.objects.filter(auther="jungmin").first()
    return render(request, 'cornell.html', {'mynotes': mynotes})

def cnDetail(request):
    mynotes = Mynote.objects.filter(auther="jungmin").first()
    return render(request, 'cornellDetail.html', {'mynotes': mynotes})

def update(request):
    if request.method == "POST":
        input_title = request.POST['title']
        input_k1 = request.POST['k1']
        input_k2 = request.POST['k2']
        input_k3 = request.POST['k3']
        input_k4 = request.POST['k4']
        input_k5 = request.POST['k5']
        input_note = request.POST['note']
        input_summary = request.POST['summary']

        mynote = Mynote.objects.filter(auther="jungmin").first()
        mynote.title = input_title
        mynote.keyword1 = input_k1
        mynote.keyword2 = input_k2
        mynote.keyword3 = input_k3
        mynote.keyword4 = input_k4
        mynote.keyword5 = input_k5
        mynote.content = input_note
        mynote.summary = input_summary
        mynote.save()
        
    return render(request, 'update.html')

def resultPage(request):
    return render(request, 'result.html')

def creditPage(request):
    return render(request, 'credit.html')


    
