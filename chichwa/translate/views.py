from django.shortcuts import render
from .services import translator

# Create your views here.


def translate(request):
    translator.translate_text("Hello ","en","sw")
    return render(request,"index.html")