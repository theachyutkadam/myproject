from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.loginUser),
    path('logout', views.logoutUser),
    path('contact', views.contact),

]
