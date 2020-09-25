from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
    path('', views.index),
    path('myweb/', include('myweb.urls', namespace="myweb")),
    path('admin/', admin.site.urls),
    path('one/', views.one),
]
