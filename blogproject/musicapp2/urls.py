from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', musicsub2, name="musicsub2"),
    path('musicnew2/', musicnew2, name="musicnew2"),
    path('musicedit2/<str:id>', musicedit2, name="musicedit2"),
    path('musicdelete2/<str:id>', musicdelete2, name="musicdelete2"),
]
