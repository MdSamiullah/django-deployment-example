from django.urls import path # in django 1.10, from django.conf.urls import url
from help_app import views

urlpatterns = [
    path('', views.help, name='help'),
]
