from django.shortcuts import render
import requests

# Create your views here.

def main(request):
    context = {}
    return render(request, "index.html", context)

def register(request):
    context = {}
    return render(request, "register.html", context)

def signin(request):
    context = {}
    return render(request, "signin.html", context)

def faq(request):
    context = {}
    return render(request, "faq.html", context)

def partner(request):
    context = {}
    return render(request, "partner.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)

def blog(request):
    context = {}
    return render(request, "blog.html", context)
