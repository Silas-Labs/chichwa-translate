from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('v1/translate-text', views.translate), 
]
