# Generated by Django 3.1.7 on 2021-04-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0035_auto_20210407_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='subpoena',
            field=models.FileField(default='', upload_to='temp/'),
            preserve_default=False,
        ),
    ]
