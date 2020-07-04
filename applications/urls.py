from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django_pdfkit import PDFView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('function/', views.functionPage, name="functionPage"),
    path('streaming/', views.streamingPage, name="streamingPage"),
    path('cornell/', views.cornellPage, name="cornellPage"),
    path('cornell/detail', views.cnDetail, name="cnDetail"),
    path('result/', views.resultPage, name="resultPage"),
    path('credit/', views.creditPage, name="creditPage"),
    path('notepost/', views.notepost, name="notepost"),
]