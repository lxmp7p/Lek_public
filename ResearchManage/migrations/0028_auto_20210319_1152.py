# Generated by Django 3.1.7 on 2021-03-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0027_auto_20210318_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='another_doc_expertize',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='another_materials',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='brochure_researcher',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='conclusion_ethics',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='date_created',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='dublicat_dogovor',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='form_inf_list',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='formular_request',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='info_med_company',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='info_payout',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='last_solutions',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='permission_FS',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='polozhenie_o_soglasii',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='program_klin_research',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='registration_cards',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='rukovodstvo',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='secretar_accepted',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='teamList',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='technical_file',
            field=models.FileField(upload_to='temp/'),
        ),
        migrations.AlterField(
            model_name='medproductrequestresearch',
            name='version_science_bio',
            field=models.FileField(upload_to='temp/'),
        ),
    ]
