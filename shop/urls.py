from django.contrib import admin
from django.urls import path,include
from shop import views
from users import views as users_views
from django.contrib.auth import views as authentication_views

app_name = 'shop'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/',views.detail , name='detail'),
]