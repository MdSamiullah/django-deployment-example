from django.shortcuts import render
from django.http import HttpResponse
from users_app.models import users
from . import forms
# Create your views here.

def index(request):
    # return HttpResponse("<em> Hello world! </em>")
    users_list = users.objects.order_by("firstName")
    user_dict = {'entry_list':users_list}
    # my_dict = {'insert_me':"Hello I am from first_app/index.html  !"}
    return render(request, 'users_app/users.html', context=user_dict)

def form_name_view (request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something here code
                print("Validation success")
                print("Name:" + form.cleaned_data['name'])
                print("Email:" + form.cleaned_data['email'])
                print("Text:" + form.cleaned_data['text'])

    return render(request, 'users_app/form_page.html', {'form':form})
