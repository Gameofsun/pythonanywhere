from django.urls import path
from . import views
from django.contrib import admin
#from django.conf.urls import url


app_name = 'myweb'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('',views.Register, name="Register"),
    path('',views.Login, name="Login"),
    path('',views.comment, name="comment"),
    path('',views.Rating, name="Rating")










]