# Generated by Django 3.1.7 on 2021-02-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0014_auto_20210225_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votelist',
            name='meeting_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='votelist',
            name='research',
            field=models.CharField(max_length=10),
        ),
    ]
