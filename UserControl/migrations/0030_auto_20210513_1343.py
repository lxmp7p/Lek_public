# Generated by Django 3.1.7 on 2021-05-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0029_auto_20210504_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(max_length=30, verbose_name='Номер телефона'),
        ),
    ]
