# Generated by Django 3.1.7 on 2021-04-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0034_mkifirstrequestresearch_addedinmeeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='medproductrequestresearch',
            name='addedInMeeting',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='addedInMeeting',
            field=models.BooleanField(default=False),
        ),
    ]