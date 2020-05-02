from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My second project</em>")

def help(request):
    # return HttpResponse("<em> Hello world! </em>")
    my_dict = {'add_content_from_views_py':"Hello I am from help_app/help.html  !"}
    return render(request, 'help_app/help.html', context=my_dict)
