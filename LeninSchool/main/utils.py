from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Новости', 'url_name': 'news'},
    {'title': 'Сотрудники', 'url_name': 'employees'},
    # {'title': 'О нас', 'url_name': 'about_us'},
    # {'title': 'Обратная связь', 'url_name': 'contact_us'},
    {'title': 'Правило школы', 'url_name': 'school_rules'},
    {'title': 'Добавить_статью', 'url_name': 'addpage'},
    {'title': 'Расписания', 'url_name': 'raspisanie'},
    {'title': 'Домашнии_задании', 'url_name': 'homeworks'},
    {'title': 'Классы', 'url_name': 'classes'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        post = Employees.objects.all()
        all_news = News.objects.all()
        all_employees = Employees.objects.all()
        raspisanie = AddRaspisanie.objects.all()
        rules = SchoolRulesModel.objects.all()
        homeworks = HomeworkModel.objects.all()
        classes = ClassCategory.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(6)
        if not self.request.user.is_superuser:
            user_menu.pop(5)
            user_menu.pop(7)

        context['menu'] = user_menu
        context['all_news'] = all_news
        context['all_employees'] = all_employees
        context['p'] = post
        context['raspisanie'] = raspisanie
        context['rules'] = rules
        context['homeworks'] = homeworks
        context['classes'] = classes

        return context
