# Generated by Django 4.2.1 on 2023-05-18 15:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='Название класса')),
                ('slug', models.SlugField(max_length=3, unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фимилия')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('info', models.TextField(null=True, verbose_name='Контент')),
                ('email', models.EmailField(max_length=255, verbose_name='Почта')),
                ('phone', models.IntegerField(verbose_name='Номер телефона пр. (996701500422)')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/employees/%Y/', verbose_name='Фотография')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/employees/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Документ в pdf формате')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Загаловок')),
                ('content', models.TextField(verbose_name='Контент')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/news/%Y/%m/%d/', verbose_name='Фотография')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/news/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'avi', 'flm', 'ogg'])], verbose_name='Видео')),
                ('audio', models.FileField(blank=True, null=True, upload_to='musics/news/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MP3', 'mp3', 'ogg', 'wav', 'tac', 'adx', 'flac', 'wma', 'aac', 'opus', 'm4a', 'ape', 'pac', 'flac'])], verbose_name='Аудио')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/news/%Y/%m/%d/', verbose_name='Файл')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-time_create', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SchoolRulesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Загаловок')),
                ('rules', models.TextField(verbose_name='Правило')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Правило',
                'verbose_name_plural': 'Правилы',
                'ordering': ['-time_create', 'id'],
            },
        ),
        migrations.CreateModel(
            name='AddRaspisanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_url_slug', models.SlugField(max_length=3, unique=True, verbose_name='URL')),
                ('day1example1', models.CharField(max_length=30, verbose_name='День 1 урок 1')),
                ('day1example2', models.CharField(max_length=30, verbose_name='День 1 урок 2')),
                ('day1example3', models.CharField(max_length=30, verbose_name='День 1 урок 3')),
                ('day1example4', models.CharField(max_length=30, verbose_name='День 1 урок 4')),
                ('day1example5', models.CharField(max_length=30, verbose_name='День 1 урок 5')),
                ('day1example6', models.CharField(max_length=30, verbose_name='День 1 урок 6')),
                ('day2example1', models.CharField(max_length=30, verbose_name='День 2 урок 1')),
                ('day2example2', models.CharField(max_length=30, verbose_name='День 2 урок 2')),
                ('day2example3', models.CharField(max_length=30, verbose_name='День 2 урок 3')),
                ('day2example4', models.CharField(max_length=30, verbose_name='День 2 урок 4')),
                ('day2example5', models.CharField(max_length=30, verbose_name='День 2 урок 5')),
                ('day2example6', models.CharField(max_length=30, verbose_name='День 2 урок 6')),
                ('day3example1', models.CharField(max_length=30, verbose_name='День 3 урок 1')),
                ('day3example2', models.CharField(max_length=30, verbose_name='День 3 урок 2')),
                ('day3example3', models.CharField(max_length=30, verbose_name='День 3 урок 3')),
                ('day3example4', models.CharField(max_length=30, verbose_name='День 3 урок 4')),
                ('day3example5', models.CharField(max_length=30, verbose_name='День 3 урок 5')),
                ('day3example6', models.CharField(max_length=30, verbose_name='День 3 урок 6')),
                ('day4example1', models.CharField(max_length=30, verbose_name='День 4 урок 1')),
                ('day4example2', models.CharField(max_length=30, verbose_name='День 4 урок 2')),
                ('day4example3', models.CharField(max_length=30, verbose_name='День 4 урок 3')),
                ('day4example4', models.CharField(max_length=30, verbose_name='День 4 урок 4')),
                ('day4example5', models.CharField(max_length=30, verbose_name='День 4 урок 5')),
                ('day4example6', models.CharField(max_length=30, verbose_name='День 4 урок 6')),
                ('day5example1', models.CharField(max_length=30, verbose_name='День 5 урок 1')),
                ('day5example2', models.CharField(max_length=30, verbose_name='День 5 урок 2')),
                ('day5example3', models.CharField(max_length=30, verbose_name='День 5 урок 3')),
                ('day5example4', models.CharField(max_length=30, verbose_name='День 5 урок 4')),
                ('day5example5', models.CharField(max_length=30, verbose_name='День 5 урок 5')),
                ('day5example6', models.CharField(max_length=30, verbose_name='День 5 урок 6')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.classcategory', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Расписания',
                'verbose_name_plural': 'Расписании',
                'ordering': ['-time_create', 'id'],
            },
        ),
    ]
