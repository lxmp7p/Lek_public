# Generated by Django 3.1.7 on 2021-04-26 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0039_auto_20210423_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='logAboutResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='mkifirstrequestresearch',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResearchManage.logaboutresearch'),
        ),
    ]
