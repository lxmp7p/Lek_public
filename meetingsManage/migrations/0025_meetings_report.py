# Generated by Django 3.1.7 on 2021-03-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0024_votelist_type_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='report',
            field=models.FileField(default='', upload_to='temp/'),
            preserve_default=False,
        ),
    ]
