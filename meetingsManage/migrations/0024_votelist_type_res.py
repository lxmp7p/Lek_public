# Generated by Django 3.1.7 on 2021-03-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0023_auto_20210319_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='votelist',
            name='type_res',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
