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
import os, sys
from PIL import Image, ImageDraw, ImageFont
import img2pdf

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

def downloadCornell(request):
    createCornell()
    imgToPdf('applications/static/img/cornell.jpg')

    response = HttpResponse(open('applications/static/pdf/cornell.pdf', 'rb').read())
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename=cornell.pdf'
    return response

def createCornell():
    mynote = Mynote.objects.filter(auther="jungmin").first()

    title = mynote.title
    summary = mynote.summary
    
    keywordList = []
    if (mynote.keyword1 is not None):
        keywordList.append(mynote.keyword1)
    else:
        keywordList.append("")
    if (mynote.keyword2 is not None):
        keywordList.append(mynote.keyword2)
    else:
        keywordList.append("")
    if (mynote.keyword3 is not None):
        keywordList.append(mynote.keyword3)
    else:
        keywordList.append("")
    if (mynote.keyword4 is not None):
        keywordList.append(mynote.keyword4)
    else:
        keywordList.append("")
    if (mynote.keyword5 is not None):
        keywordList.append(mynote.keyword5)
    else:
        keywordList.append("")

    content = mynote.content
    listNum = int(len(content)/38)
    if (len(content) != listNum*38):
        listNum = listNum + 1

    contentList = []
    currentLen = 0
    for i in range(0,9):
        if (currentLen + 38 >= len(content)):
            contentList.append(content[currentLen:])
            for j in range(i+1,9):
                contentList.append("")
            break
        else:
            contentList.append(content[38*i:38*(i+1)])
            currentLen = 38*(i+1)

    img = Image.open("applications/static/img/note.jpg")
    fontTiSu = ImageFont.truetype("applications/static/font/nseb.ttf", 30, encoding="UTF-8")
    fontKeCo = ImageFont.truetype("applications/static/font/nsb.ttf", 20, encoding="UTF-8")
 
    # title
    posTitleX = 50
    posTitleY = 30
    # keyword
    posKeywordX = 20
    posKeywordY = [100, 135, 170, 205, 240]
    # content
    posContentX = 220
    posContentY = [100, 135, 170, 205, 240, 275, 310, 345, 380]
    # summary
    posSummaryX = 50
    posSummaryY = 500

    d = ImageDraw.Draw(img)

    # title
    d.text((posTitleX, posTitleY), title, font=fontTiSu, fill='black')

    # keyword
    d.text((posKeywordX, posKeywordY[0]), keywordList[0], font=fontKeCo, fill='black')
    d.text((posKeywordX, posKeywordY[1]), keywordList[1], font=fontKeCo, fill='black')
    d.text((posKeywordX, posKeywordY[2]), keywordList[2], font=fontKeCo, fill='black')
    d.text((posKeywordX, posKeywordY[3]), keywordList[3], font=fontKeCo, fill='black')
    d.text((posKeywordX, posKeywordY[4]), keywordList[4], font=fontKeCo, fill='black')
    
    # content
    d.text((posContentX, posContentY[0]), contentList[0], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[1]), contentList[1], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[2]), contentList[2], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[3]), contentList[3], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[4]), contentList[4], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[5]), contentList[5], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[6]), contentList[6], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[7]), contentList[7], font=fontKeCo, fill='black')
    d.text((posContentX, posContentY[8]), contentList[8], font=fontKeCo, fill='black')

    # summary
    d.text((posSummaryX, posSummaryY), summary, font=fontTiSu, fill='black')

    img.save('applications/static/img/cornell.jpg')

def imgToPdf(img):
    with open("applications/static/pdf/cornell.pdf","wb") as f:
	    f.write(img2pdf.convert(img))

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


    
