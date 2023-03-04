from django.contrib import admin
from django.urls import path
from base.views import index, forJsonResponse, forPost


urlpatterns = [
    path('', index),
    path('salom/', forJsonResponse),
    path('check/', forPost)
]
