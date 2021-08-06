from django.urls import path
from .views import *

urlpatterns = [
    path('acc_login/', acc_login, name = "acc_login"),
    path('acc_logout/', acc_logout, name = "acc_logout"),
    path('acc_register/', acc_register, name = "acc_signup"),
]
