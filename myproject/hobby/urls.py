from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>',hsub, name="hsub"),
    path('hnew/', hnew, name="hnew"),
    path('hedit/<str:id>', hedit, name="hedit"),
    path('hdelete/<str:id>', hdelete, name="hdelete"),
    path('email/',email, name="email"),
    path('mmain/', mmain, name="mmain"),
    path('msend/', msend, name="msend"),
    path('mnew/', mnew, name="mnew"),
    path('mmain/<str:id>', msub, name="msub"),
]