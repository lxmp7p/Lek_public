from unittest import TestCase
from django.test import Client
from django.contrib.auth.models import User
from UserControl.models import User
from django.test import SimpleTestCase
from UserControl.forms import UserForm
from datetime import date, timedelta

# class ClientMixin:
#     def setUp(self) -> None:
#         self.client = Client()
#         self.credentials = {
#             'username': 'testUsers',
#             'password': 'passwords'}
#         User.objects.create_user(**self.credentials)


#     def tearDown(self) -> None:
#         User.objects.filter(username='testUsers').delete()
#         print(self.__class__)


# class TestIndexPage(ClientMixin, TestCase):
#     def test_index_available(self):  #Тест открытия главной страницы
#         response = self.client.get('/', self.credentials, follow=True)
#         self.assertEqual(response.status_code, 200)


# class TestRegistration(ClientMixin, TestCase):
#     def test_open_page(self):    #Тест открытия страницы регистрации
#         response = self.client.get('/registration/', self.credentials, follow=True)
#         self.assertEqual(response.status_code, 200)

class TestForms(TestCase):
    def test_valid_registration(self):     #Тест валидной формы регистрации пользователя
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_valid_registration")
        self.assertTrue(form.is_valid())

    def test_eng_letters_in_names_registration(self):     #Тест формы регистрации пользователя с английскими буквами в  ФИО
        form=UserForm(data={
            'username':'TestUsername2',
            'first_name':'TestFirstName',
            'last_name':'TestLastName',
            'middle_name':'TestMiddleName',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_eng_letters_in_names_registration")
        self.assertFalse(form.is_valid())

    def test_numbers_in_names_registration(self):     #Тест формы регистрации пользователя с цифрами в  ФИО
        form=UserForm(data={
            'username':'TestUsername2',
            'first_name':'124124',
            'last_name':'214124',
            'middle_name':'124124',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_numbers_in_names_registration")
        self.assertFalse(form.is_valid())

    
    def test_short_phone_registration(self):     #Тест формы регистрации пользователя с коротким номером телефона
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'2',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_short_phone_registration")
        self.assertFalse(form.is_valid())
    
    def test_long_phone_registration(self):     #Тест формы регистрации пользователя с длинным номером телефона
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'2222222222222222222222222',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_long_phone_registration")
        self.assertFalse(form.is_valid())
    
    def test_literals_in_phone_registration(self):     #Тест формы регистрации пользователя с буквами вместо телефона
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'aaaaaaaaaaa',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_literals_in_phone_registration")
        self.assertFalse(form.is_valid())

    def test_short_pass_registration(self):     #Тест формы регистрации пользователя с коротким паролем
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'2Tf',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_short_pass_registration")
        self.assertFalse(form.is_valid())

    def test_weak_pass_registration(self):     #Тест формы регистрации пользователя со слабым паролем
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'aaaaaaaaaaaaaa',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_weak_pass_registration")
        self.assertFalse(form.is_valid())

    def test_long_pass_registration(self):     #Тест формы регистрации пользователя с слишком большим паролем
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_long_pass_registration")
        self.assertFalse(form.is_valid())

    def test_bad_username_registration(self):     #Тест формы регистрации пользователя с невалидным символом в username
        form=UserForm(data={
            'username':'TestUsername7#',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_bad_username_registration")
        self.assertFalse(form.is_valid())
    
    def test_bad_mail_registration(self):     #Тест формы регистрации пользователя с невалидной почтой
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'Test@ru.',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*5)
            })
        print("test_bad_mail_registration")
        self.assertFalse(form.is_valid())
    
    def test_small_birth_date_registration(self):     #Тест формы регистрации пользователя с датой рождения < 18 лет
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000)
            })
        print("test_small_birth_date_registration")
        self.assertFalse(form.is_valid())

    def test_big_birth_date_registration(self):     #Тест формы регистрации пользователя с датой рождения > 140 лет
        form=UserForm(data={
            'username':'TestUsername1',
            'first_name':'Абоба',
            'last_name':'Абоба',
            'middle_name':'Абоба',
            'email':'TestEmail@mail.ru',
            'password':'TestPassword2',
            'phone_number':'88888888888',
            'sex':'Мужчина',
            'birth_date':date.today()-timedelta(days=2000*100)
            })
        print("test_big_birth_date_registration")
        self.assertFalse(form.is_valid())