from django.urls import path # in django 1.10, from django.conf.urls import url
from school_app import views
from school_app.views import IndexView, SchoolDetailView, SchoolListView

app_name = "school_app"

urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    path('<int:pk>/', SchoolDetailView.as_view(), name='detail'),
]
