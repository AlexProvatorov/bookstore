from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    SetPasswordForm, PasswordResetForm
from .models import User


class RegistrationForm(UserCreationForm):
    """
    Форма для регистрации.
    """
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """
    Форма для аутентификации.
    """
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))


class UserForgotPasswordForm(PasswordResetForm):
    """
    Форма для восстановления пароля.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Форма для установки нового пароля.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


