from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.TextField('Роль',)

    def __str__(self):
        return self.name 
        
class PositionList(models.Model):
    name = models.TextField()


class User(AbstractUser):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=150)
    middle_name = models.CharField('Отчество', max_length=30)
    email = models.EmailField('Почта')
    docStatus = models.CharField(max_length=30)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role', null=True, blank=True)
    docStatus = models.CharField(max_length=100)
    #------------------------Мужик начал-------------------------
    phone_number = models.IntegerField('Номер телефона', max_length=30)
    #-----------------------Мужик закончил-----------------------
    birth_date = models.DateField('Дата рождения', null=True, max_length=10)
    password = models.CharField('Пароль', max_length=50)
    registration_accepted = models.CharField('Подтвердить регистрацию',max_length=10)
    photo = models.FileField(upload_to='user_photo/', blank=True, null=True)
    sex = models.CharField('Пол', max_length=30)

    class Meta(object):
        unique_together = ('email',)

    def __unicode__(self):
        return self.phone_number

class PositionUserList(models.Model):
    position = models.ForeignKey(PositionList, on_delete=models.CASCADE, related_name='position')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='position_user')
    status = models.CharField(max_length=100)

class PI_BirthDay(models.Model):
	FIO = models.CharField(max_length=10000,)

	def __str__(self):
		return '%s' % (self.FIO)


class DocsTypeList(models.Model):
    name = models.CharField(max_length=100)

class DocsList(models.Model):
    docName = models.ForeignKey(DocsTypeList, on_delete=models.CASCADE, related_name='DocsType')
    file = models.FileField(upload_to='temp/', blank=True, null=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userOwnerDocs')

