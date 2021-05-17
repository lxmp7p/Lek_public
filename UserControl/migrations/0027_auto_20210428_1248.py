# Generated by Django 3.1.7 on 2021-04-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0026_auto_20210428_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.CharField(max_length=10, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=30, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=30, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=30, verbose_name='Пол'),
        ),
    ]
