from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите Ваше имя')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.IntegerField(min_value=1, max_value=110, label='Введите возраст')

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Ваше имя')
#     email = forms.CharField(label='email')
#     message = forms.CharField(widget=forms.Textarea, label='Сообщение')
#     subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку')
