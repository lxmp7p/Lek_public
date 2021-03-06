# Generated by Django 3.1.3 on 2020-11-25 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ResearchManage', '0007_mkifirstrequestresearch_secretar_accepted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetings', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='researchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='research', to='ResearchManage.mkifirstrequestresearch')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=100)),
                ('researchList', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='researchsToMeeting', to='meetingsManage.researchlist')),
                ('userList', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userList', to='meetingsManage.userlist')),
            ],
        ),
    ]
