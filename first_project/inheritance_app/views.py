from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'inheritance_app/index.html')

def other(request):
    return render(request, 'inheritance_app/other.html')

def admin(request):
    return render(request, 'inheritance_app/admin.html')
