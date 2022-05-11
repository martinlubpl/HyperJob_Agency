from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy


# Create your views here.

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html',
                      context={'vacancies': Vacancy.objects.all()})
