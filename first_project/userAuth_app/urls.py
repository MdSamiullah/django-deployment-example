from django.urls import path # in django 1.10, from django.conf.urls import url
from userAuth_app import views

app_name = "userAuth_app"

urlpatterns = [
    path('', views.index, name='indexUrlName'),
    path('register/', views.register, name='registerUrlName'),
    path('login/', views.user_login, name='loginURLName'),
]
