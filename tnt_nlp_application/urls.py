from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('tnt-nlp/admin/', admin.site.urls),
    path('tnt-nlp/', include('applications.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)