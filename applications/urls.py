from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cornell', views.cornell, name="cornell"),
    path('download', views.downloadCornell, name="downloadCornell"),
    path('cornell/update', views.update, name="update"),
]