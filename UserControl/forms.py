from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import User
from .models import Role
from django.utils.translation import ugettext_lazy as _
from django.forms import PasswordInput, Select, ClearableFileInput
import re
from django.contrib.auth.validators import ASCIIUsernameValidator
import datetime
from django.core.exceptions import ValidationError

SpecialSym=['$','@','#','!','?','%','^','&','*','(',')','-']
my_choices = ( ('Man', 'Мужской'), ('Woman', 'Женский'))

class DateInput(forms.DateInput):
    input_type = 'date'

class EmailInput(forms.EmailInput):
    input_type = 'email'

class NumberInput(forms.NumberInput):
    input_type = 'number'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'middle_name', 'sex', 'birth_date', 'phone_number', 'email', 'password',)
        
        labels = {
            'sex': _('Пол'),
            'username': _('Логин'),
            #-----------------------Мужик начал-----------------------
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
            'middle_name': _('Отчество'),
            #----------------------Мужик закончил---------------------
            'phone_number': _('Номер телефона'),
            'birth_date': _('Дата рождения'),
        }

        widgets = {
            'sex': Select(choices=my_choices),
            'password': PasswordInput(),
            'birth_date': DateInput(),
            'email': EmailInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        #-----------------------Мужик начал-----------------------
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['middle_name'].required = True
        #----------------------Мужик закончил---------------------
        username_validator = ASCIIUsernameValidator()
        self.fields['username'].validators=[username_validator]
        self.fields['username'].max_length = 30
        #-----------------------Мужик начал-----------------------
        self.fields['password'].required = True
        self.fields['password'].max_length = 50
        
    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        print(birth_date.year > datetime.date.today().year - 18)
        if birth_date.year > datetime.date.today().year - 18 or birth_date.year<datetime.date.today().year-140:
            raise forms.ValidationError("Неверная дата")
        return birth_date
       
        #вродь пофиксил
    def clean_first_name(self):
        UserFirstName = self.cleaned_data['first_name']
        if re.search('[0-9]', UserFirstName) is not None:
            raise forms.ValidationError(
                _("Имя не может включать в себя цифры")
        )
        elif re.search('[a-zA-Z]', UserFirstName) is not None:
            raise forms.ValidationError(
                _("Имя должно быть написанно кириллицей")
        )
        elif not set(r".,:;!_*-+()/#¤%&№\'").isdisjoint(UserFirstName):
            raise forms.ValidationError(
                _("Имя не должно содержать спец. символы")
        )
        return UserFirstName

    def clean_last_name(self):
        UserLastName = self.cleaned_data['last_name']
        if re.search('[0-9]', UserLastName) is not None:
            raise forms.ValidationError(
                _("Фамилия не может включать в себя цифры")
        )
        elif re.search('[a-zA-Z]', UserLastName) is not None:
            raise forms.ValidationError(
                _("Фамилия должна быть написанна кириллицей")
        )
        elif not set(r".,:;!_*-+()/#¤%&№\'").isdisjoint(UserLastName):
            raise forms.ValidationError(
                _("Фамилия не должна содержать спец. символы")
        )  
        return UserLastName

    def clean_middle_name(self):        
        UserMiddleName = self.cleaned_data['middle_name']
        if re.search('[0-9]', UserMiddleName) is not None:
            raise forms.ValidationError(
                _("Отчество не может включать в себя цифры")
        ) 
        elif re.search('[a-zA-Z]', UserMiddleName) is not None:
            raise forms.ValidationError(
                _("Отчество должно быть написанно кириллицей")
        )  
        elif not set(r".,:;!_*-+()/#¤%&№\'").isdisjoint(UserMiddleName):
            raise forms.ValidationError(
                _("Отчество не должно содержать спец. символы")
        )  
        return UserMiddleName

    def clean_phone_number(self):
        UserPhone=self.cleaned_data['phone_number']
        if not re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',str(UserPhone)):
            raise forms.ValidationError(
            _('Ваш телефон должен иметь следующий вид: +7 xxx-xxx-xxx или 8 xxx-xxx-xxx')
        )
        return UserPhone

    def clean_password(self):
        #SpecialSym=['$','@','#','!','?','%','^','&','*','(',')','-'] Если нужен пароль по-сложнее добавь что-то такое
        UserPass=self.cleaned_data['password']
        if len(UserPass)<8 or len(UserPass)>50:
            raise forms.ValidationError(
            _('Пароль должен быть в границах от 8 до 50 символов')
        )
        elif re.search('[0-9]', UserPass) is None:
            raise forms.ValidationError(
            _('Пароль должен содержать цифры')
        )
        elif re.search('[A-Z]', UserPass) is None:
            raise forms.ValidationError(
            _('Пароль должен содержать как минимум 1 заглавную латинскую букву')
        )
        elif re.search('[а-яёЁА-Я]', UserPass) is not None:
           raise forms.ValidationError(
            _('Пароль не должен содержать кириллицу')
        )
        return UserPass  
        #-----------------------Мужик закончил-----------------------
class UserAccept(forms.ModelForm):
    class Meta:
        model = User
        fields = ('role',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('photo',)
