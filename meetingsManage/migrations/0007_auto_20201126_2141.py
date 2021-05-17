# Generated by Django 3.1.3 on 2020-11-26 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetingsManage', '0006_auto_20201125_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='status',
            field=models.CharField(default='False', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='researchlist',
            name='meeting_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetingsManage.meetings'),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='meeting_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetingsManage.meetings'),
        ),
    ]