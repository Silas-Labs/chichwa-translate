from django.urls import path
from . import views

urlpatterns = [
    path('v1/translate-text', views.translate), 
]
