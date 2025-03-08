import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def validate_fio(value):
    if not re.match(r'^[А-Яа-яЁё\s]+$', value):
        raise forms.ValidationError('ФИО должно содержать только буквы кириллицы и пробелы.')


def validate_phone(value):
    if not re.match(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', value):
        raise forms.ValidationError('Телефон должен быть в формате +7(XXX)-XXX-XX-XX.')


class UserRegisterForm(UserCreationForm):
    fio = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Введите ФИО (символы кириллицы и пробелы)'
        }),
        label='ФИО',
        validators=[validate_fio],
    )
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Введите номер в формате +7(XXX)-XXX-XX-XX',
        }),
        label='Номер телефона',
        validators=[validate_phone],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'fio', 'phone', 'password1', 'password2', 'email']
