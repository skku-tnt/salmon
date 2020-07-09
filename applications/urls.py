from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('function/', views.functionPage, name="functionPage"),
    path('streaming/', views.streamingPage, name="streamingPage"),
    path('cornell/', views.cornellPage, name="cornellPage"),
    path('cornell/detail', views.cnDetail, name="cnDetail"),
    path('cornell/download', views.downloadCornell, name="downloadCornell"),
    path('cornell/detail/update', views.update, name="update"),
]