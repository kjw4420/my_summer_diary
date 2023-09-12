from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/',include('Detail.urls')),
    path('accounts/',include('user.urls')),
    path('',user.views.index),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
