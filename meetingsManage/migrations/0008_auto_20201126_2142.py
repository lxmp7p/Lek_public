# Generated by Django 3.1.3 on 2020-11-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0007_auto_20201126_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researchlist',
            old_name='meeting_id',
            new_name='meeting',
        ),
        migrations.RenameField(
            model_name='userlist',
            old_name='meeting_id',
            new_name='meeting',
        ),
    ]
