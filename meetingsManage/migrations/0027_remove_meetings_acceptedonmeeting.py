# Generated by Django 3.1.7 on 2021-03-24 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0026_meetings_acceptedonmeeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='acceptedOnMeeting',
        ),
    ]
