# Generated by Django 3.1.7 on 2021-03-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0009_auto_20210225_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='PI_BirthDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=10000)),
                ('City', models.CharField(max_length=10000)),
                ('birthday', models.DateField()),
            ],
        ),
    ]
