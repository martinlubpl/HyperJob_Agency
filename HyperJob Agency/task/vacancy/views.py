from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden


# Create your views here.

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html',
                      context={'vacancies': Vacancy.objects.all()})


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            description = request.POST['description']
            if request.user.is_staff:
                Vacancy.objects.create(description=description,
                                       author=request.user)
                return redirect('/home')
            else:
                return HttpResponseForbidden()
        return HttpResponseForbidden()
