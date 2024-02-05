from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegistrationForm, LoginForm


# Create your views here.


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        old_context = {
            'title': 'Регистрация',
            'content': 'Регистрация «BOOK STORE»',
        }
        return dict(list(context.items()) + list(old_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        old_context = {
            'title': 'Авторизация',
            'content': 'Авторизация «BOOK STORE»',
        }
        return dict(list(context.items()) + list(old_context.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
