# Generated by Django 3.1.7 on 2021-02-25 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0012_votelist_meeting_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votelist',
            name='meeting_id',
        ),
    ]
