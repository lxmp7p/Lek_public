# Generated by Django 3.1.7 on 2021-05-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0058_auto_20210517_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotherdocuments',
            name='ver',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anotherdocumentshistory',
            name='ver',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
