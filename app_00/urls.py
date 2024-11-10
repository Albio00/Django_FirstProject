from django.urls import path
from app_00 import views

urlpatterns = [
    path('', views.index, name='index'),
]