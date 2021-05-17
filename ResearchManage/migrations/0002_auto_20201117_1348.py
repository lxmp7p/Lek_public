# Generated by Django 3.1.3 on 2020-11-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='adversting',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='cast_research',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='name_research',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='owner_request',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='predsedatel_accepted',
        ),
        migrations.RemoveField(
            model_name='mkifirstrequestresearch',
            name='secretar_accepted',
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='accept_research_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='accept_research_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='advertising',
            field=models.FileField(blank=True, null=True, upload_to='advertising/'),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='another_doc_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='another_doc_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher',
            field=models.FileField(blank=True, null=True, upload_to='form_inf/'),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='cast_researcher_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='contract_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='form_inf_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='form_inf_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='name_another_doc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='owner',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='protocol_research_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='protocol_research_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='version',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='accept_research',
            field=models.FileField(blank=True, null=True, upload_to='accept_research/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='another_doc',
            field=models.FileField(blank=True, null=True, upload_to='another_doc/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='contract',
            field=models.FileField(blank=True, null=True, upload_to='contract/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='form_inf',
            field=models.FileField(blank=True, null=True, upload_to='form_inf/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='list_members',
            field=models.FileField(blank=True, null=True, upload_to='list_members/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='main_researcher',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='protocol_research',
            field=models.FileField(blank=True, null=True, upload_to='protocol_research/'),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='ver_bio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='write_objects',
            field=models.FileField(blank=True, null=True, upload_to='write_objects/'),
        ),
    ]