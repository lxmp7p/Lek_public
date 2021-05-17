# Generated by Django 3.1.7 on 2021-03-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20210303_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggerrecords',
            name='ip',
        ),
        migrations.AddField(
            model_name='loggerrecords',
            name='username',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
