from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('experience/', views.experience, name="experience"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)