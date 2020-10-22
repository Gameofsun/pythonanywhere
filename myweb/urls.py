from django.urls import path
from . import views
from django.contrib import admin


app_name = 'myweb'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('',views.Register, name="Register"),
    path('',views.Login, name="Login"),









]