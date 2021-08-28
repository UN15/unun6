from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>',bsub, name="bsub"),
    path('bnew/', bnew, name="bnew"),
    path('bedit/<str:id>', bedit, name="bedit"),
    path('bdelete/<str:id>', bdelete, name="bdelete"),
    path('hashtag/', hashtag, name="hashtag"),
    path('search/', blist, name="search"),
]