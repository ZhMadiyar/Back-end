from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения task")

def cat(request, cat_id):
    return HttpResponse(f"<h1>Категории</h1><p> id: {cat_id} </p>")

def cat_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Категории</h1><p> slug: {cat_slug} </p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p> {year} </p>")
