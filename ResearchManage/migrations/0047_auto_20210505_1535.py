# Generated by Django 3.1.7 on 2021-05-05 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0046_auto_20210504_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher_date',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher_version',
        ),
    ]
