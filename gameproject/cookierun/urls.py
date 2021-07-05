from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', gamesub, name="gamesub"),
    path('gamenew/', gamenew, name="gamenew"),
    path('gameedit/<str:id>', gameedit, name="gameedit"),
    path('gamedelete/<str:id>', gamedelete, name="gamedelete"),
]