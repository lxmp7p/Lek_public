# Generated by Django 3.1.7 on 2021-03-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0016_user_docstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docslist',
            name='status',
        ),
        migrations.AddField(
            model_name='docslist',
            name='statuss',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
