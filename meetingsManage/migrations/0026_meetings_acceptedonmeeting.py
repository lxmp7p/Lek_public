# Generated by Django 3.1.7 on 2021-03-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0025_meetings_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='acceptedOnMeeting',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
