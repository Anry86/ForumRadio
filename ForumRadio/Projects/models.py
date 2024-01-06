from django.db import models
from django.urls import reverse_lazy  # импортируем библиотеку ленивой загрузки


# Модель Projects. Тут находится созданные проекты
class Projects(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')                      # название проекта
    content = models.TextField(blank=True, verbose_name='Текст')                            # содержание проекта
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')     # время создания проекта
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')        # время изменения проекта
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Медиа')
    # если добавить в скобки blank=True, то поле станет обязательное к заполнению

    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def get_absolute_url(self):
        return reverse_lazy('View_Pro', kwargs={'pk': self.pk})
    # View_Pro - ссылается на файл urls.py

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['created_at']      # сортировка по времени создания created_at (-created_at - обратный порядок)
