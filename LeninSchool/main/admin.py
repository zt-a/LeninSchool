from django.contrib import admin

from main.models import *


class EmloyeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'status', 'email', 'phone', 'photo', 'time_update', 'is_published')
    list_display_links = ('id', 'name', 'surname')
    search_fields = ('name', 'surname', 'status', 'email', 'phone')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name', 'surname')}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'video', 'file', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'time_create', 'file', 'time_update')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}



class ClassCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class RasAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'class_name')
    search_fields = ('id', 'class_name', 'time_create', 'time_update',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'class_url_slug': ('class_name',)}


class SchoolRulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rules', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'name', 'time_create', 'time_update',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'nameTeacher', 'forTheClass', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'topic')
    search_fields = ('id', 'topic', 'nameTeacher', 'forTheClass', 'time_create', 'time_update',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

admin.site.register(Employees, EmloyeesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(AddRaspisanie, RasAdmin)
admin.site.register(SchoolRulesModel, SchoolRulesAdmin)
admin.site.register(ClassCategory, ClassCategoryAdmin)
admin.site.register(HomeworkModel, HomeworkAdmin)


# admin
# DevZhyrgal
# 1794zhyrgal20061113

