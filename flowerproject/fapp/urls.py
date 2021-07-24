from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>',fsub, name="fsub"),
    path('fnew/', fnew, name="fnew"),
    path('fedit/<str:id>', fedit, name="fedit"),
    path('fdelete/<str:id>', fdelete, name="fdelete"),
    path('search/', list, name="search"),
]