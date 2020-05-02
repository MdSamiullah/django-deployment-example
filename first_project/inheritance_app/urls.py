from django.urls import path # in django 1.10, from django.conf.urls import url
from inheritance_app import views

app_name = "inheritance_app"

urlpatterns = [
    path('', views.index, name='indexUrlName'), # it helps to make the following work: http://127.0.0.1:8000/inheritance
    path('other/', views.other, name='otherUrlName'), # it helps to make the following work: http://127.0.0.1:8000/inheritance/other/
]
