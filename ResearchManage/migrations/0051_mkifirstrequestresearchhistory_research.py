# Generated by Django 3.1.7 on 2021-05-13 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResearchManage', '0050_auto_20210513_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='mkifirstrequestresearchhistory',
            name='research',
            field=models.ForeignKey(default=54, on_delete=django.db.models.deletion.CASCADE, related_name='research_h', to='ResearchManage.mkifirstrequestresearch'),
            preserve_default=False,
        ),
    ]
