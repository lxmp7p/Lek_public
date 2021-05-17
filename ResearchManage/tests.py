from django.test import TestCase
from django.core.files import File
from ResearchManage.forms import ResearchFormMKI
from django.test import Client
from unittest import TestCase, mock
from datetime import date, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile
import os
# Create your tests here.

class TestForms(TestCase):
    def test_valid_ResearchFormMKI_form(self):     #Тест валидной формы первичной подачи заявки
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'wb') as f:
        	f.write(b"ABOBA")
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'rb') as f:
        	testfile=f.read()
        	form=ResearchFormMKI(data={
            	'protocol_number':'224',
            	'description':'Ну мы тут тестим тесты',
            	'main_researcher':1,
            	'ver_bio':'Тесты тестов',
            	'version':'Тестовая',
            	'cast_researcher_date':date.today()-timedelta(days=2000*5),
            	'accept_research_version':'Тестовая версия',
            	'accept_research_date':date.today()-timedelta(days=2000*5),
            	'protocol_research_version':'Тестовая версия',
            	'protocol_research_date':date.today()-timedelta(days=2000*5),
            	'contract_date':date.today()-timedelta(days=2000*5),
            	'name_another_doc':'Тест',
            	'another_doc_version':'Тестовая',
            	'another_doc_date':date.today()-timedelta(days=2000*5)
            	},
            	files={'another_doc': SimpleUploadedFile('another_doc', testfile),
            	'contract': SimpleUploadedFile('contract', testfile),
            	'advertising': SimpleUploadedFile('advertising', testfile),
            	'write_objects': SimpleUploadedFile('write_objects', testfile),
            	'protocol_research': SimpleUploadedFile('protocol_research', testfile),
            	'accept_research': SimpleUploadedFile('accept_research', testfile),
            	'form_inf': SimpleUploadedFile('form_inf', testfile),
            	'cast_researcher': SimpleUploadedFile('cast_researcher', testfile),
            	'list_members': SimpleUploadedFile('list_members', testfile),
            	'document': SimpleUploadedFile('document', testfile)
        	})
        os.remove(os.path.abspath(os.curdir)+"Test.txt")
        print(form.errors)
        print("test_valid_ResearchFormMKI_form")
        self.assertTrue(form.is_valid())

    def test_wrong_data_ResearchFormMKI_form(self):     #Тест формы первичной подачи заявки с датой доков>сегодня.На момент написания тест кейс провальный!
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'wb') as f:
        	f.write(b"ABOBA")
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'rb') as f:
        	testfile=f.read()
        	form=ResearchFormMKI(data={
            	'protocol_number':'224',
            	'description':'Ну мы тут тестим тесты',
            	'main_researcher':1,
            	'ver_bio':'Тесты тестов',
            	'version':'Тестовая',
            	'cast_researcher_date':date.today()+timedelta(days=2000*5),
            	'accept_research_version':'Тестовая версия',
            	'accept_research_date':date.today()+timedelta(days=2000*5),
            	'protocol_research_version':'Тестовая версия',
            	'protocol_research_date':date.today()+timedelta(days=2000*5),
            	'contract_date':date.today()+timedelta(days=2000*5),
            	'name_another_doc':'Тест',
            	'another_doc_version':'Тестовая',
            	'another_doc_date':date.today()+timedelta(days=2000*5)
            	},
            	files={'another_doc': SimpleUploadedFile('another_doc', testfile),
            	'contract': SimpleUploadedFile('contract', testfile),
            	'advertising': SimpleUploadedFile('advertising', testfile),
            	'write_objects': SimpleUploadedFile('write_objects', testfile),
            	'protocol_research': SimpleUploadedFile('protocol_research', testfile),
            	'accept_research': SimpleUploadedFile('accept_research', testfile),
            	'form_inf': SimpleUploadedFile('form_inf', testfile),
            	'cast_researcher': SimpleUploadedFile('cast_researcher', testfile),
            	'list_members': SimpleUploadedFile('list_members', testfile),
            	'document': SimpleUploadedFile('document', testfile)
        	})
        os.remove(os.path.abspath(os.curdir)+'Test.txt')
        print(form.errors)
        print("test_wrong_data_ResearchFormMKI_form")
        self.assertFalse(form.is_valid())
    def test_wrong_file_format_ResearchFormMKI_form(self):     #Тест формы первичной подачи заявки с несуществующим типом файла.На момент написания тест кейс провальный!
        #TODO:расширить до каждого отдельного поля
        with open(os.path.abspath(os.curdir)+'Test.aboba', 'wb') as f:
        	f.write(b"ABOBA")
        with open(os.path.abspath(os.curdir)+'Test.aboba','rb') as f:
        	testfile=f.read()
        	form=ResearchFormMKI(data={
            	'protocol_number':'224',
            	'description':'Ну мы тут тестим тесты',
            	'main_researcher':1,
            	'ver_bio':'Тесты тестов',
            	'version':'Тестовая',
            	'cast_researcher_date':date.today()-timedelta(days=2000*5),
            	'accept_research_version':'Тестовая версия',
            	'accept_research_date':date.today()-timedelta(days=2000*5),
            	'protocol_research_version':'Тестовая версия',
            	'protocol_research_date':date.today()-timedelta(days=2000*5),
            	'contract_date':date.today()-timedelta(days=2000*5),
            	'name_another_doc':'Тест',
            	'another_doc_version':'Тестовая',
            	'another_doc_date':date.today()-timedelta(days=2000*5)
            	},
            	files={'another_doc': SimpleUploadedFile('another_doc', testfile),
            	'contract': SimpleUploadedFile('contract', testfile),
            	'advertising': SimpleUploadedFile('advertising', testfile),
            	'write_objects': SimpleUploadedFile('write_objects', testfile),
            	'protocol_research': SimpleUploadedFile('protocol_research', testfile),
            	'accept_research': SimpleUploadedFile('accept_research', testfile),
            	'form_inf': SimpleUploadedFile('form_inf', testfile),
            	'cast_researcher': SimpleUploadedFile('cast_researcher', testfile),
            	'list_members': SimpleUploadedFile('list_members', testfile),
            	'document': SimpleUploadedFile('document', testfile)
        	})
        os.remove(os.path.abspath(os.curdir)+'Test.aboba')
        print(form.errors)
        print("test_wrong_file_format_ResearchFormMKI_form")
        self.assertFalse(form.is_valid())

    def test_empty_main_researcher_format_ResearchFormMKI_form(self):     #Тест формы первичной подачи заявки с невыбранным главным исследователем
        with open(os.path.abspath(os.curdir)+'Test.txt', 'wb') as f:
        	f.write(b"ABOBA")
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'rb') as f:
        	testfile=f.read()
        	form=ResearchFormMKI(data={
            	'protocol_number':'224',
            	'description':'Ну мы тут тестим тесты',
            	'main_researcher':None,
            	'ver_bio':'Тесты тестов',
            	'version':'Тестовая',
            	'cast_researcher_date':date.today()-timedelta(days=2000*5),
            	'accept_research_version':'Тестовая версия',
            	'accept_research_date':date.today()-timedelta(days=2000*5),
            	'protocol_research_version':'Тестовая версия',
            	'protocol_research_date':date.today()-timedelta(days=2000*5),
            	'contract_date':date.today()-timedelta(days=2000*5),
            	'name_another_doc':'Тест',
            	'another_doc_version':'Тестовая',
            	'another_doc_date':date.today()-timedelta(days=2000*5)
            	},
            	files={'another_doc': SimpleUploadedFile('another_doc', testfile),
            	'contract': SimpleUploadedFile('contract', testfile),
            	'advertising': SimpleUploadedFile('advertising', testfile),
            	'write_objects': SimpleUploadedFile('write_objects', testfile),
            	'protocol_research': SimpleUploadedFile('protocol_research', testfile),
            	'accept_research': SimpleUploadedFile('accept_research', testfile),
            	'form_inf': SimpleUploadedFile('form_inf', testfile),
            	'cast_researcher': SimpleUploadedFile('cast_researcher', testfile),
            	'list_members': SimpleUploadedFile('list_members', testfile),
            	'document': SimpleUploadedFile('document', testfile)
        	})
        os.remove(os.path.abspath(os.curdir)+'Test.txt')
        print(form.errors)
        print("test_empty_main_researcher_format_ResearchFormMKI_form")
        self.assertFalse(form.is_valid())

    def test_empty_char_fields_format_ResearchFormMKI_form(self):     #Тест формы первичной подачи заявки с незаполненными полями для символьного ввода
        #TODO:расширить до каждого отдельного поля
        with open(os.path.abspath(os.curdir)+'Test.txt', 'wb') as f:
        	f.write(b"ABOBA")
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'rb') as f:
        	testfile=f.read()
        	form=ResearchFormMKI(data={
            	'protocol_number':None,
            	'description':None,
            	'main_researcher':1,
            	'ver_bio':None,
            	'version':None,
            	'cast_researcher_date':date.today()-timedelta(days=2000*5),
            	'accept_research_version':None,
            	'accept_research_date':date.today()-timedelta(days=2000*5),
            	'protocol_research_version':None,
            	'protocol_research_date':date.today()-timedelta(days=2000*5),
            	'contract_date':date.today()-timedelta(days=2000*5),
            	'name_another_doc':None,
            	'another_doc_version':None,
            	'another_doc_date':date.today()-timedelta(days=2000*5)
            	},
            	files={'another_doc': SimpleUploadedFile('another_doc', testfile),
            	'contract': SimpleUploadedFile('contract', testfile),
            	'advertising': SimpleUploadedFile('advertising', testfile),
            	'write_objects': SimpleUploadedFile('write_objects', testfile),
            	'protocol_research': SimpleUploadedFile('protocol_research', testfile),
            	'accept_research': SimpleUploadedFile('accept_research', testfile),
            	'form_inf': SimpleUploadedFile('form_inf', testfile),
            	'cast_researcher': SimpleUploadedFile('cast_researcher', testfile),
            	'list_members': SimpleUploadedFile('list_members', testfile),
            	'document': SimpleUploadedFile('document', testfile)
        	})
        os.remove(os.path.abspath(os.curdir)+'Test.txt')
        print(form.errors)
        print("test_empty_char_fields_format_ResearchFormMKI_form")
        self.assertFalse(form.is_valid())

    def test_empty_date_fields_ResearchFormMKI_form(self):     #Тест формы первичной подачи заявки с пустыми значениями полей даты На момент написания тест кейс провальный!
    	#TODO:расширить до каждого отдельного поля
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'wb') as f:
        	f.write(b"ABOBA")
        with open(os.path.abspath(os.curdir)+'Test.txt' ,'rb') as f:
        	testfile=f.read()
        	form=ResearchFormMKI(data={
            	'protocol_number':'224',
            	'description':'Ну мы тут тестим тесты',
            	'main_researcher':1,
            	'ver_bio':'Тесты тестов',
            	'version':'Тестовая',
            	'cast_researcher_date':None,
            	'accept_research_version':'Тестовая версия',
            	'accept_research_date':None,
            	'protocol_research_version':'Тестовая версия',
            	'protocol_research_date':None,
            	'contract_date':None,
            	'name_another_doc':'Тест',
            	'another_doc_version':'Тестовая',
            	'another_doc_date':None
            	},
            	files={'another_doc': SimpleUploadedFile('another_doc', testfile),
            	'contract': SimpleUploadedFile('contract', testfile),
            	'advertising': SimpleUploadedFile('advertising', testfile),
            	'write_objects': SimpleUploadedFile('write_objects', testfile),
            	'protocol_research': SimpleUploadedFile('protocol_research', testfile),
            	'accept_research': SimpleUploadedFile('accept_research', testfile),
            	'form_inf': SimpleUploadedFile('form_inf', testfile),
            	'cast_researcher': SimpleUploadedFile('cast_researcher', testfile),
            	'list_members': SimpleUploadedFile('list_members', testfile),
            	'document': SimpleUploadedFile('document', testfile)
        	})
        os.remove(os.path.abspath(os.curdir)+'Test.txt')
        print(form.errors)
        print("test_empty_date_fields_ResearchFormMKI_form")
        self.assertTrue(form.is_valid())