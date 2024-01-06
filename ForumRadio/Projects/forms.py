# формы создания нового пользователя и нового проекта

from django import forms
from .models import Projects
import re  # импортируем регулярные выражения
from django.core.exceptions import ValidationError  # импортируем ошибки валидации
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # имп. модель формы юзера и аунтефикации
from django.contrib.auth.models import User  # импортируем модель юзера
# from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ProForm(forms.ModelForm):     # форма для создания нового проекта

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValueError('Имя не должно начинаться с цифр')
        return name

    class Meta:
        model = Projects
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 20
            }),
            'category': forms.Select(attrs={  # выпадающий список
                'class': 'form-control'
            })
        }
    # captcha = CaptchaField()

#    name = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(attrs={
#        'class': 'form-conttol'
#    }))
#    password = forms.CharField(label='Пароль', required=False, widget=forms.Textarea(attrs={
#        'class': 'form-conttol',
#        'rows': 2
#    }))
#    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия',
#                                      empty_label='Виберите профессию', widget=forms.Select(attrs={
#            'class': 'form-control'
#        }))    # выпадающий список
