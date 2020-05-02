from django.shortcuts import render

from django.http import HttpResponse
from signup_app.forms import NewUserForm

# Create your views here.


def index(request):
    return render(request, 'signup_app/index.html')

def signUp(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error! Form is invalid")
    return render(request, 'signup_app/signup.html', {'form':form})
