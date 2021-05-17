# Generated by Django 3.1.7 on 2021-05-04 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0044_auto_20210427_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameAnotherDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AnotherDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_research', models.CharField(max_length=100)),
                ('type_research', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=100)),
                ('name_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_document', to='ResearchManage.nameanotherdocument')),
            ],
        ),
    ]
