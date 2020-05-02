from django.urls import path # in django 1.10, from django.conf.urls import url
from signup_app import views

urlpatterns = [
    path('', views.signUp, name=''), # it seems it does not matter if name = "" or name = "something else" unless you use relative URL and inheritance template
]
