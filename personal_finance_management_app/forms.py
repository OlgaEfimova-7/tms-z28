from django import forms
GENDER = (('Мужской', 'М'), ('Женский', 'Ж'))


class RegistrationFormForConsumer(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    age = forms.IntegerField(label='Возраст')
    gender = forms.ChoiceField(choices=GENDER, label='Пол')
    email = forms.EmailField(max_length=254, label='Email')
    city = forms.CharField(max_length=100, label='Город')
    login = forms.CharField(max_length=100, label='Логин')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Пароль')


class LogInToPersonalAccountForm(forms.Form):
    login = forms.CharField(max_length=100, label='Логин')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Пароль')


class ChequeUploadForm(forms.Form):
    """ Cheque upload form """
    cheque = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Загрузите фото чека')
