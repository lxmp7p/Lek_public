# Generated by Django 3.1.7 on 2021-03-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0013_auto_20210302_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='accept_research',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='advertising',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='form_inf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='list_members',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='protocol_research',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='write_objects',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]