from django.shortcuts import render
from .services import translator
import json
from django.http import JsonResponse

# Create your views here.

def translate(request):
    if request.method != "POST":
        return JsonResponse(
            {"error" : "only POST method allowed"},
            status= 403
        )
    
    try:
        body = json.loads(request.body)
        text = body.get("text")
        target_lang = body.get("target_lang")
        source_lang = body.get("source_lang")
        translated = None
        
        if not text or not target_lang or not source_lang:
            return JsonResponse(
                {"error" : "missing required fields"}
            )
        


        translated = translator.translate_text(text, source_lang, target_lang)
        return JsonResponse({"translated":translated})
    
    except json.JSONDecodeError:
        return JsonResponse(
            {"error" : "Invalid JSON"},
            status = 400
        )
    

def index(request):
    if request.method == "POST" :
        body = json.loads(request.body)
        text = body.get("text")
        target_lang = body.get("target_lang")
        source_lang = body.get("source_lang")
        
        translated = translator.translate_text(text, source_lang, target_lang)

    return render(request,"index.html", {"translated":translated})