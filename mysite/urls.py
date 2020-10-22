from django.contrib import admin
from django.urls import path, include
from myweb import views


urlpatterns = [
    path('', views.Login),
    path('index', views.index),
    path('one/', views.one),
    #path('two/', views.two),
    path('myweb/', include('myweb.urls', namespace="myweb")),
    path('admin/', admin.site.urls),
    path('Register/',views.Register),


    #ตั้งชื่อpathแล้วแต่ชอบ  ตามด้วยชื่อ viewที่สร้างสร้างใน views.py
    #path('registeration/', RegisterUserView, name='register_user'),
]