from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', musicsub, name = "musicsub"),
    path('musicnew/', musicnew, name = "musicnew"),
    path('musicedit/<str:id>', musicedit, name = "musicedit"),
    path('musicdelete/<str:id>', musicdelete, name = "musicdelete"),
]
