# Generated by Django 3.1.7 on 2021-03-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0028_votelist_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votelist',
            name='datetime',
            field=models.CharField(max_length=100),
        ),
    ]