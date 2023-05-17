from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Загаловок')
    # slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), label='URL')
    # content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}), label='Контент')
    # photo = forms.CharField(label='Фото (необезательно)', required=False, widget=forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}))
    # # audio = forms.FileField(label='Аудио' (необезательно), required=False, widget=forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}), validators=[FileExtensionValidator(allowed_extensions=['MP3', 'mp3', 'ogg', 'wav', 'tac', 'adx', 'flac', 'wma', 'aac', 'opus', 'm4a', 'ape', 'pac', 'flac'])])
    # # video = forms.FileField(label='Видео (необезательно)', required=False, widget=forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}), validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'avi', 'flm', 'ogg'])])
    # # file = forms.FileField(label='Файл (необезательно)', required=False, widget=forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}))
    # is_published = forms.BooleanField(label='Публикация', required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}))
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрано', widget=forms.Select(attrs={'class': 'custom-select'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cat'].empty_label = 'Категория не выбрано'
        self.fields['cat'].queryset = Category.objects.all()

        self.fields['is_published'].reqired = False
        self.fields['is_published'].initial = True

        self.fields['photo'].label = 'Фото (необезательно)'
        self.fields['photo'].reqired = False

        # self.fields['audio'].label = 'Аудио (необезательно)'
        # self.fields['audio'].reqired = False
        #
        # self.fields['video'].label = 'Видео (необезательно)'
        # self.fields['video'].reqired = False
        #
        # self.fields['file'].label = 'Файл (необезательно)'
        # self.fields['file'].reqired = False

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
            'photo': forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}),
            # 'audio': forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}),
            # 'video': forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}),
            # 'file': forms.TextInput(attrs={'class': 'custom-file-input', 'type': 'file'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
            'cat': forms.Select(attrs={'class': 'custom-select'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'name_reg form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'name_reg form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'name_reg form-control'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'email form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password form-control'}))
    password2 = forms.CharField(label='Потверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'password form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'name_reg form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password form-control'}))