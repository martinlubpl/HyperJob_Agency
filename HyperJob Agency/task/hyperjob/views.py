from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class HyperLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class HyperSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {'create': 'none'}
        if request.user.is_authenticated:
            if request.user.is_staff:
                context['create'] = 'vacancy'
            else:
                context['create'] = 'resume'
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        raise PermissionDenied()
