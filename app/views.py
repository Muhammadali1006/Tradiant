from django.shortcuts import HttpResponse, render

def home(request):
    return render(request, "app/base.html")

def about(request):
    return render(request, "app/new.html")

def why(request):
    return render(request, "app/why.html")