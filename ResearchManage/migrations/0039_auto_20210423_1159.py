# Generated by Django 3.1.7 on 2021-04-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0038_conflictsinterests'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conflictsinterests',
            options={},
        ),
        migrations.AddField(
            model_name='mkifirstrequestresearch',
            name='secretar_accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
