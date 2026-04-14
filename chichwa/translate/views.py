from django.shortcuts import render
from .services import translator

# Create your views here.


def translate(request):
    translated = None
    if request.method == 'POST':
        source_lang = request.POST.get('source_lang')
        target_lang = request.POST.get('target_lang')
        text = request.POST.get('text')

        translated = translator.translate_text(text, source_lang, target_lang)
    return render(request,"index.html", {"translated": translated})
    