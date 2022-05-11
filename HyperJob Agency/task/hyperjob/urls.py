"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from hyperjob.views import IndexView, HyperLoginView, HyperSignupView
from resume.views import ResumeView
from vacancy.views import VacancyView
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('resumes', ResumeView.as_view(), name='resume'),
    path('vacancies', VacancyView.as_view(), name='vacancy'),
    path('login', HyperLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', HyperSignupView.as_view(), name='signup'),
    path('login/', RedirectView.as_view(url='/login'), name='login'),
    path('logout/', RedirectView.as_view(url='/logout'), name='logout'),
    path('signup/', RedirectView.as_view(url='/signup'), name='signup'),
]
