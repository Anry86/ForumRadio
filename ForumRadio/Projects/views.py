# контроллеры
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages  # сообщения на форме сайта
from django.contrib.auth import login, logout

from .models import Projects           # импортируем модель Projects
from .forms import ProForm, UserRegisterForm, UserLoginForm


# регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            # return redirect('Login')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'Projects/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'Projects/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Login')


# функция страницы самого сайта Проектов по электронике
class HomePro(ListView):
    model = Projects                                # получаем модель БД Projects
    context_object_name = 'projects'                #
    template_name = 'Projects/home_pro_list.html'   # шаблон страницы
    extra_context = {'title': 'Проекты'}            #
    paginate_by = 3                                 # кол-во новостей на странице

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'        # получаем в контекст в поле шаблона title текст 'Главная страница'
        return context

    def get_queryset(self):
        return Projects.objects.all()


class ViewPro(DetailView):      # просмотр отдельной новости
    model = Projects
    context_object_name = 'news_item'
    template_name = 'Projects/view_pro.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title        # получаем в контекст title текущего проекта
        return context                              # отправляем контекст шаблону

class AddPro(CreateView):     # добавление проекта
    form_class = ProForm
    template_name = 'Projects/add_pro.html'
    login_url = '/admin/'


class NewsByCategory(ListView):  # отображение новостей по категориям
    model = Projects
    template_name = 'Forum/home_pro_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3  # кол-во новостей на странице

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Projects.objects.get(pk=self.kwargs['category_id']).title  # название категории
        return context

    def get_queryset(self):
        return Projects.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


# это функция главной страницы приветствия
def index(request):
    return render(request, 'index.html', {'title': 'Добро пожаловать на форум по электронике и программированию'})
    # render - отвечает за отрисовку запрошенных страниц
    # request - запрос от браузера
    # 'index.html' - отображаемый шаблон страницы
    # {'title': 'Список новостей'} - контекст, с которым будет взаимодействовать шаблон index.html
    # 'title': 'Список новостей' - заголовок
