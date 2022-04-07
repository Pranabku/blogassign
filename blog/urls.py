
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ path('',views.index),
                path('login',views.Login, name='login'),
                path('profile',views.Profile,name='profile')
                ]
