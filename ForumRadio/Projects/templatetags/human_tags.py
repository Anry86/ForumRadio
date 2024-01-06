from ..models import Projects  # две точки - поиск нужного файла с модулем в предыдущем каталоге
from django import template

register = template.Library()


@register.simple_tag(name='get_list_pro')   # обращается файл templatetags/ink/_sidebar.html - боковой список -->
def get_projects():
    return Projects.objects.all()

