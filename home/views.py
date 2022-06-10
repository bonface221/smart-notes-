from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):
    form_class=UserCreationForm
    template_name= 'home/register.html'
    success_url='/smart/notes'

    def get(self,request,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super().get(request,*args, **kwargs)


def logoutUser(request):
    logout(request)
    return redirect('home')


class LoginInterfaceView(LoginView):
    template_name= 'home/login.html'


class HomeView(TemplateView):
    template_name= 'home/welcome.html'
    extra_context= dict(today=datetime.now())


