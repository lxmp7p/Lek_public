# Generated by Django 3.1.7 on 2021-05-17 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0059_auto_20210517_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anotherdocuments',
            name='ver',
        ),
    ]
