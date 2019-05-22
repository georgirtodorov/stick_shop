from django.urls import path
from . import views
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    path('', views.landing, name='landing')

]