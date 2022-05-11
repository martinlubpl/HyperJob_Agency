from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden


# Create your views here.

class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resumes.html',
                      context={'resumes': Resume.objects.all()})


class NewResumeView(View):
    def post(self, request):
        if request.user.is_authenticated:
            description = request.POST['description']
            if request.user.is_staff:
                return HttpResponseForbidden()
            else:
                Resume.objects.create(description=description,
                                      author=request.user)
                return redirect('/home')
        else:
            # raise PermissionDenied()
            return HttpResponseForbidden()
