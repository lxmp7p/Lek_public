from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import MkiFirstRequestResearch, MedProductRequestResearch
from UserControl.models import User
from django.forms import ModelForm, FileInput, TextInput, Select, ChoiceField, ClearableFileInput
from django.utils.translation import ugettext_lazy as _
from UserControl.models import PI_BirthDay



CHOICES = [('1', 'First'), ('2', 'Second')]
class TimeInput(forms.TimeInput):
    input_time = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'

class ResearchFormMKI(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearchFormMKI, self).__init__(*args, **kwargs)
        # access object through self.instance...
        self.fields['main_researcher'].queryset = PI_BirthDay.objects.all()

    class Meta:
        model = MkiFirstRequestResearch
        exclude = ()
        fields = ('protocol_number','description', 'document', 'main_researcher','list_members',
                  'ver_bio', 'accept_research', 'accept_research_version', 'accept_research_date', 'protocol_research', 'protocol_research_version',
                  'protocol_research_date', 'contract', 'contract_date', 'advertising', 'write_objects', 'name_another_doc',
                  'another_doc', 'another_doc_version', 'another_doc_date',
                  )
        widgets = {
            'accept_research': FileInput(),
            'version': TextInput(),
            'accept_research_date': DateInput(),
            'protocol_research_date': DateInput(),
            'cast_researcher_date': DateInput(),
            'contract_date': DateInput(),
            'another_doc_date': DateInput(),
            'cast_researcher': ClearableFileInput(attrs={'multiple': True}),
            'form_inf': ClearableFileInput(attrs={'multiple': True}),
        }
        labels = {
            'protocol_number': _('Номер протокола'),
            'description': _('Название протокола'),
            'document': _('Заявление'),
            'main_researcher': _('Главный исследователь'),
            'list_members': _('Загрузите список членов команды'),
            'ver_bio': _('Версия биографии'),
            'accept_research': _('Загрузите разрешение МЗ РФ (необязательно)'),
            'accept_research_version': _('Номер документа (необязательно)'),
            'accept_research_date': _('Дата (необязательно)'),
            'protocol_research': _('Загрузите протокол исследования'),
            'protocol_research_version': _('Версия документа'),
            'protocol_research_date': _('Дата'),
            'contract': _('Загрузите договор обязательного страхования'),
            'contract_date': _('Дата'),
            'advertising': _('Загрузите образцы рекламной продукции'),
            'write_objects': _('Загрузите письменные материалы'),
            'name_another_doc': _('Название документа'),
            'another_doc': _('Документ'),
            'another_doc_version': _('Версия документа'),
            'another_doc_date': _('Дата'),
        }

class ResearchFormMKIEdit(ResearchFormMKI):
    def __init__(self, *args, **kwargs):
        super(ResearchFormMKIEdit, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = False


class MedProductRequestResearchForm(forms.ModelForm):
    class Meta:
        model = MedProductRequestResearch
        fields = ('formular_request','teamList', 'version_science_bio', 'permission_FS','conclusion_ethics',
                  'program_klin_research', 'form_inf_list', 'registration_cards', 'another_materials', 'info_payout', 'brochure_researcher',
                  'rukovodstvo', 'technical_file', 'polozhenie_o_soglasii', 'dublicat_dogovor', 'last_solutions', 'info_med_company', 'another_doc_expertize',
                  )
        labels = {
            'formular_request': _('Формуляр заявки'),
            'teamList': _('Список членов команды исследователей'),
            'version_science_bio': _('Резюме исследователя'), #изменить название столбца
            'permission_FS': _('Разрешение Федеральной службы'),
            'conclusion_ethics': _('Заключение совета по этике'),
            'program_klin_research': _('Программа клинического испытания'),
            'form_inf_list': _('Форма информационного листка'),
            'registration_cards': _('Индивидуальные регистрационные карты'),
            'another_materials': _('Различные материалы'),
            'info_payout': _('Информация о выплатах'),
            'brochure_researcher': _('Брошюра исследователя'),
            'rukovodstvo': _('Руководство по эксплуатации на мед изделие'),
            'technical_file': _('Технический файл'),
            'polozhenie_o_soglasii': _('Положение о согласии следовать этическим принципам'), 
            'dublicat_dogovor': _('Копия договора страхования'), 
            'last_solutions': _('Предыдущие решения'), 
            'info_med_company': _('Сведения о мед организациях'), 
            'another_doc_expertize': _('Иные документы'),
        }

