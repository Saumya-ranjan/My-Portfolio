from django.contrib import admin
from django.urls import path,include
from . import views
from django.http import HttpResponse

urlpatterns = [
      path('',views.home )
]
