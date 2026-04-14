from django.shortcuts import render
from .services import translator

# Create your views here.


def translate(request):
    translated = translator.translate_text("Hello","en","sw")
    return render(request,"index.html", {"translated": translated})