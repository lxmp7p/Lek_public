# Generated by Django 3.1.3 on 2020-11-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0006_mkifirstrequestresearch_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='secretar_accepted',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
