"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include,path  # in django 1.10, from django.conf.urls import include
# from first_app import views
# from help_app import views
# from users_app import views
# from signup_app import views
# from inheritance_app import views
from userAuth_app import views

urlpatterns = [

    # path(r'',views.index, name='index'),
    # # note, the udemy tutorial says the following to add instead of the previous line
    #     # url(r'^$',views.index, name='index'),
    # path(r'',views.help, name='help'),

    # path('users/', include('users_app.urls')),
    # path('help/', include('help_app.urls')),
    # path('mynewextension/', include('first_app.urls')),
    path('',views.index, name='index'),
    # # path('',views.help, name='help'),
    path('admin/', admin.site.urls),
    path('signup/', include('signup_app.urls')),
    # path('formpage/', include('users_app.urls')),
    # path('inheritance/', include('inheritance_app.urls')),
    path('userAuth/', include('userAuth_app.urls')),
    path('logout/', views.user_logout, name='logoutURLName'),
    path('special/', views.special, name='specialURLName'),
]
