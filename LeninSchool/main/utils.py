
from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Новости', 'url_name': 'news'},
    {'title': 'Сотрудники', 'url_name': 'employees'},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Обратная связь', 'url_name': 'contact_us'},
    {'title': 'Правило школы', 'url_name': 'school_rules'},
    # {'title': 'Категории', 'url_name': 'categorys'},
    # {'title': 'Добавить_статью', 'url_name': 'addpage'},
    {'title': 'Расписания', 'url_name': 'raspisanie'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        post = Employees.objects.all()
        all_news = News.objects.all()
        cats = Category.objects.all()
        all_employees = Employees.objects.all()
        raspisanie = AddRaspisanie.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(7)

        context['menu'] = user_menu
        context['cats'] = cats
        context['all_news'] = all_news
        context['all_employees'] = all_employees
        context['p'] = post
        context['raspisanie'] = raspisanie

        return context

