# Generated by Django 3.1.7 on 2021-03-05 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0016_auto_20210305_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='main_researcher',
        ),
    ]