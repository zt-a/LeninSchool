# from django.db import models

from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class Employees(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Фимилия', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    info = models.TextField(verbose_name='Контент', null=True)
    email = models.EmailField(verbose_name='Почта', max_length=255)
    phone = models.IntegerField(verbose_name='Номер телефона пр. (996701500422)')
    photo = models.ImageField(verbose_name='Фотография', upload_to='photos/employees/%Y/', null=True, blank=True)
    status = models.CharField(verbose_name='Статус', max_length=255)
    document = models.FileField(verbose_name='Документ в pdf формате', upload_to='documents/employees/%Y/%m/%d/',
                                null=True, blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf', ])])
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)


    def __str__(self):
        return f'{self.name}, {self.surname}'

    def get_absolute_url(self):
        return reverse('employees_post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Загаловок')
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(verbose_name='Фотография', upload_to='photos/news/%Y/%m/%d/', null=True, blank=True)
    video = models.FileField(verbose_name='Видео', upload_to='videos/news/%Y/%m/%d/', null=True, blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'avi', 'flm', 'ogg'])])
    audio = models.FileField(verbose_name='Аудио', upload_to='musics/news/%Y/%m/%d/', null=True, blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MP3', 'mp3', 'ogg', 'wav', 'tac', 'adx', 'flac', 'wma', 'aac',
                                                     'opus', 'm4a', 'ape', 'pac', 'flac'])])
    file = models.FileField(verbose_name='Файл', upload_to='files/news/%Y/%m/%d/', null=True, blank=True)
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'id']


class AddRaspisanie(models.Model):
    class_name = models.CharField(max_length=3, verbose_name='Класс')
    class_url_slug = models.SlugField(max_length=3, unique=True, db_index=True, verbose_name='URL')

    day1example1 = models.CharField(max_length=30, verbose_name='День 1 урок 1')
    day1example2 = models.CharField(max_length=30, verbose_name='День 1 урок 2')
    day1example3 = models.CharField(max_length=30, verbose_name='День 1 урок 3')
    day1example4 = models.CharField(max_length=30, verbose_name='День 1 урок 4')
    day1example5 = models.CharField(max_length=30, verbose_name='День 1 урок 5')
    day1example6 = models.CharField(max_length=30, verbose_name='День 1 урок 6')

    day2example1 = models.CharField(max_length=30, verbose_name='День 2 урок 1')
    day2example2 = models.CharField(max_length=30, verbose_name='День 2 урок 2')
    day2example3 = models.CharField(max_length=30, verbose_name='День 2 урок 3')
    day2example4 = models.CharField(max_length=30, verbose_name='День 2 урок 4')
    day2example5 = models.CharField(max_length=30, verbose_name='День 2 урок 5')
    day2example6 = models.CharField(max_length=30, verbose_name='День 2 урок 6')

    day3example1 = models.CharField(max_length=30, verbose_name='День 3 урок 1')
    day3example2 = models.CharField(max_length=30, verbose_name='День 3 урок 2')
    day3example3 = models.CharField(max_length=30, verbose_name='День 3 урок 3')
    day3example4 = models.CharField(max_length=30, verbose_name='День 3 урок 4')
    day3example5 = models.CharField(max_length=30, verbose_name='День 3 урок 5')
    day3example6 = models.CharField(max_length=30, verbose_name='День 3 урок 6')

    day4example1 = models.CharField(max_length=30, verbose_name='День 4 урок 1')
    day4example2 = models.CharField(max_length=30, verbose_name='День 4 урок 2')
    day4example3 = models.CharField(max_length=30, verbose_name='День 4 урок 3')
    day4example4 = models.CharField(max_length=30, verbose_name='День 4 урок 4')
    day4example5 = models.CharField(max_length=30, verbose_name='День 4 урок 5')
    day4example6 = models.CharField(max_length=30, verbose_name='День 4 урок 6')

    day5example1 = models.CharField(max_length=30, verbose_name='День 5 урок 1')
    day5example2 = models.CharField(max_length=30, verbose_name='День 5 урок 2')
    day5example3 = models.CharField(max_length=30, verbose_name='День 5 урок 3')
    day5example4 = models.CharField(max_length=30, verbose_name='День 5 урок 4')
    day5example5 = models.CharField(max_length=30, verbose_name='День 5 урок 5')
    day5example6 = models.CharField(max_length=30, verbose_name='День 5 урок 6')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse('raspisanie', kwargs={'class_slug': self.class_url_slug})

    class Meta:
        verbose_name = 'Расписания'
        verbose_name_plural = 'Расписании'
        ordering = ['-time_create', 'id']


class SchoolRulesModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Загаловок')
    rules = models.TextField(verbose_name='Правило', )
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правилы'
        ordering = ['-time_create', 'id']


class ClassCategory(models.Model):
    name = models.CharField(max_length=3, verbose_name='Название класса')
    slug = models.SlugField(max_length=3, unique=True, db_index=True, verbose_name='URL', )
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('classes', kwargs={'slug': self.slug})



    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['name', 'id']



class HomeworkModel(models.Model):
    topic = models.CharField(max_length=255, verbose_name='Тема урока или название домашний задании')
    nameTeacher = models.CharField(max_length=255, verbose_name='Ваше имя или имя учителя')
    forTheClass = models.CharField(max_length=3, verbose_name='Для какого класса')

    homework = models.TextField(verbose_name='Домашние задание')
    photo = models.ImageField(verbose_name='Фотография', upload_to='photos/news/%Y/%m/%d/', null=True, blank=True)

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Домашняя задания'
        verbose_name_plural = 'Домашнии задании'
        ordering = ['-time_create', 'id']


    def get_absolute_url(self):
        return reverse('homeworks', kwargs={'homework_slug': self.topic})



# class ListStudents(models.Model):
#     FIO = models.CharField(max_length=255, verbose_name='ФИО')
#     student_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', )
#     Class = models.CharField(max_length=3, verbose_name='Класс ученика')
#     GuardianFIO = models.CharField(max_length=255, verbose_name='ФИО отца или матери или опекуна')
#     birthday = models.DateField()
#     time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
#     time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
#     is_published = models.BooleanField(verbose_name='Публикация', default=True)
#
#
#     class Meta:
#         verbose_name = 'Ученик'
#         verbose_name_plural = 'Список учеников'
#         ordering = ['-time_create', 'id']
#
#
#     def get_absolute_url(self):
#         return reverse('students', kwargs={'student_slug': self.student_slug})