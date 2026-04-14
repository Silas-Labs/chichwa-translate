from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/v1/translate-text',views.translate)
]
