from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe   # импортируем функцию для отображения миниатюры фото на админке
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# импортируем таблицу Projects
from .models import Projects


class ProAdminForm(forms.ModelForm):
    # profession = forms.CharField(widget=CKEditorUploadingWidget())
    # было поле для редактирования текста с разметкой HTML - <p>Электрик</p>
    projects = forms.CharField()  # стала просто окно для ввода - Электрик

    class Meta:
        model = Projects  # добавил .profession
        fields = '__all__'


class ProAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'created_at')
    fields = ('title', 'content', 'photo', 'get_photo', 'created_at', 'updated_at', 'is_published') 	# тут добавляем картинку в админке, в редакторе новости
    readonly_fields = ('get_photo', 'created_at', 'updated_at')		# тут поля, которые изменять нельзя
    form = ProAdminForm

    def get_photo(self, obj):  # self, obj - функция принимает текущий объект
        if obj.photo:			# если картинка есть, то...
            return mark_safe(f'<img src="{obj.photo.url}" width="200">')
        else:					# если картинки нет, то...
            return 'Нет фото'

    get_photo_description = 'Миниатюра'		# описание поля с картинкой


admin.site.register(Projects, ProAdmin)
