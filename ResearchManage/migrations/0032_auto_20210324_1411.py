# Generated by Django 3.1.7 on 2021-03-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0031_medproductrequestresearch_acceptedonmeeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='medproductrequestresearch',
            name='report',
            field=models.FileField(default='', upload_to='temp/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='report',
            field=models.FileField(default='', upload_to='temp/'),
            preserve_default=False,
        ),
    ]
