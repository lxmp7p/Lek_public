# Generated by Django 3.2 on 2021-04-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0036_mkifirstrequestresearch_subpoena'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_research', models.CharField(max_length=100)),
                ('type_research', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='accept_research',
            field=models.FileField(blank=True, null=True, upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='accept_research_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='accept_research_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='form_inf_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='form_inf_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
