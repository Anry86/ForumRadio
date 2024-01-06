# маршруты

from django.urls import path
from .views import HomePro, AddPro, ViewPro, register, user_login, user_logout, index  # импортируем контроллеры

urlpatterns = [
    # path('', cache_page(60)(HomeNews.as_view()), name='Home'),    # кешируем на 60 секунд
    path('', index),                                                # страница приветствия
    path('pro/',            HomePro.as_view(),  name='Home'),       # обработка запроса http://127.0.0.1:8000/pro/
    path('pro/add_pro',     AddPro.as_view(),   name='Add_pro'),    # маршрут для добавления проекта
    path('pro/<int:pk>/',   ViewPro.as_view(),  name='View_Pro'),   # отображение списка по очереди
    path('pro/register',    register,           name='Register'),
    path('pro/login/',      user_login,         name='Login'),
    path('pro/logout/',     user_logout,        name='Logout')
]
