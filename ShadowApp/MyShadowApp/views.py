from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def shadow_statement(request):
    text = request.GET.get("text", "")
    length = request.GET.get("length", None)

    if not text:
        return JsonResponse({"error": "Please provide a text parameter"}, status=400)

    if length:
        try:
            length = int(length)
            text = text[:length]
        except ValueError:
            return JsonResponse({"error": "Length must be an integer"}, status=400)

    shadow = "".join("*" if char != " " else " " for char in text)

    return JsonResponse({"original": text, "shadow": shadow, "length": len(text)})