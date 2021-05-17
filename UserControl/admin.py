from django.contrib import admin
from django import forms
# Register your models here.
from .models import User
from django.forms import Select
from django.contrib.auth import hashers


def check_ru(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return alphabet.isdisjoint(text.lower())

class PersonAdminForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'last_name', 'first_name', 'middle_name', 'sex', 'birth_date', 'phone_number', 'email', 'password', 'role', 'registration_accepted', ]

	def clean_password(self):
		return hashers.make_password(self.cleaned_data["password"])

	def clean_username(self):
		if not check_ru(self.cleaned_data["username"]):
			raise forms.ValidationError("Логин не должен содержать русские буквы")
		return self.cleaned_data["username"]


@admin.register(User)
class User(admin.ModelAdmin):
	form = PersonAdminForm

	def get_form(self, request, obj=None, **kwargs):
		my_choices = ( ('True', 'Да'), ('False', 'Нет'))
		sex = ( ('Man', 'Мужской'), ('Woman', 'Женский'))
		form = super().get_form(request, obj, **kwargs)
		form.base_fields["registration_accepted"].widget = Select(choices=my_choices)
		form.base_fields["sex"].widget = Select(choices=sex)
		return form













