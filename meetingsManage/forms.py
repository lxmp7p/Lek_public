from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Meetings
from UserControl.models import User
from django.forms import DateField, DateInput, SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from datetime import date
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meetings

        fields = ('date', 'time',
                  )

        labels = {
            'date': _('Дата'),
            'time': _('Время'),
        }
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
        
    def clean_date(self):
        date = self.cleaned_data['date']
        if date.year > datetime.date.today().year + 2 or date.day < datetime.date.today().day - 1: 
            raise forms.ValidationError("Неверная дата")
        return date




