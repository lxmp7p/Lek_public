# Generated by Django 3.1.7 on 2021-03-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0010_pi_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
