from django.urls import path # in django 1.10, from django.conf.urls import url
from users_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.form_name_view, name='form_name_view'),
    # path('signup/', views.users, name='users'),
]

# http://127.0.0.1:8000/users/formpage/ it does work
