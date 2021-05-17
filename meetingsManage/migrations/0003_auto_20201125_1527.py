# Generated by Django 3.1.3 on 2020-11-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0002_research_meeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchlist',
            name='research',
        ),
        migrations.RemoveField(
            model_name='userlist',
            name='user',
        ),
        migrations.AddField(
            model_name='meetings',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetings',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='meetings',
            name='researchList',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='meetings',
            name='time',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='meetings',
            name='userList',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Research',
        ),
        migrations.DeleteModel(
            name='researchList',
        ),
        migrations.DeleteModel(
            name='userList',
        ),
    ]
