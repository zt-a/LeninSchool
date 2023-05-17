from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .utils import *


class MainHome(DataMixin, ListView):
    template_name = 'main/index.html'
    context_object_name = 'main'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


def index(request):
    context = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'main/index.html', context=context)


class NewsViews(DataMixin, ListView):
    paginate_by = 5
    model = News
    template_name = 'main/news.html'
    context_object_name = 'all_news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Новости')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


def news(request):
    all_news = News.objects.all()
    context = {
        'title': 'Новости',
        'menu': menu,
        'all_news': all_news,
    }

    return render(request, 'main/news.html', context=context)


class ShowPostNews(DataMixin, ListView):
    model = News
    template_name = 'main/post.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Новость')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(slug=self.kwargs['post_slug'], is_published=True)


def show_post_news(request, post_id):
    post = get_object_or_404(News, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': 'Новость',
    }

    return render(request, 'main/post.html', context=context)


def show_post_news(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': 'Новость',
    }

    return render(request, 'main/post.html', context=context)

class AboutUsView(DataMixin, ListView):
    model = None
    template_name = 'main/about_us.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return

def about_us(request):
    context = {
        'title': 'О нас',
        'menu': menu,
    }
    return render(request, 'main/about_us.html', context=context)


class ContactUsView(DataMixin, ListView):
    model = None
    template_name = 'main/contact_us.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return


def contact_us(request):
    context = {
        'title': 'Обратная связь',
        'menu': menu,
    }
    return render(request, 'main/contact_us.html', context=context)

class EmployeesView(DataMixin, ListView):
    paginate_by = 10
    model = Employees
    template_name = 'main/employees.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Сотрудники')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Employees.objects.filter(is_published=True)


def employees(request):
    all_employees = Employees.objects.all()
    context = {
        'all_employees': all_employees,
        'title': 'Сотрудники',
        'menu': menu,
    }

    return render(request, 'main/employees.html', context=context)


class ShowPostEmpoyeesView(DataMixin, ListView):
    model = Employees
    template_name = 'main/show_post_employe.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Сотрудник')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Employees.objects.filter(is_published=True)

def show_post_employees(request, post_slug):
    post = get_object_or_404(Employees, slug=post_slug)

    context = {
        'p': post,
        'menu': menu,
        'title': 'Сотрудник',

    }

    return render(request, 'main/show_post_employe.html', context=context)


class SchoolRulesView(DataMixin, ListView):
    model = None
    template_name = 'main/school_rules.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Школьные правило')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return None

def school_rules(request):
    context = {
        'title': 'Школьные правило',
        'menu': menu,
    }
    return render(request, 'main/school_rules.html', context=context)


class RegisterView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_queryset(self):
        return

def register(request):
    context = {
        'title': 'Регистрация',
        'menu': menu,
    }
    return render(request, 'main/register.html', context=context)



class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

def log_in(request):
    context = {
        'title': 'Авторизация',
        'menu': menu,
    }
    return render(request, 'main/login.html', context=context)


def profile_user(request):
    context = {
        'menu': menu,
        'title': 'Профиль',
    }
    return render(request, 'main/profile.html', context=context)


class CategoryView(DataMixin, ListView):
    model = Category
    template_name = 'main/category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Category.objects.all()


def category(request, cat_slug):
    context = {
        'menu': menu,
        'title': 'Категория',
        'cat_selected': cat_slug,
    }
    return render(request, 'main/category.html', context=context)


class CategorysView(DataMixin, ListView):
    model = Category
    template_name = 'main/categorys.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категории')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Category.objects.all()

def categorys(requset):
    context = {
        'menu': menu,
        'title': 'Категории',
    }
    return render(requset, 'main/categorys.html', context=context)


class AddPageView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')

        return dict(list(context.items()) + list(c_def.items()))

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Добавить статью',
    }
    return render(request, 'main/addpage.html', context=context)



def rasView(request):
    raspisanie = AddRaspisanie.objects.all()
    context = {
        'menu': menu,
        'title': 'Расписания',
        'raspisanie_name': raspisanie

    }
    return render(request, 'main/raspisanie.html', context=context)

def rasViewClasses(request, class_slug):
    raspisanie = get_object_or_404(AddRaspisanie, class_url_slug=class_slug)
    context = {
        'menu': menu,
        'title': 'Расписания',
        'ras': raspisanie
    }

    return render(request, 'main/ras_class.html', context=context)