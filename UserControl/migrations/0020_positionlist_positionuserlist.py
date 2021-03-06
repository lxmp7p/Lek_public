# Generated by Django 3.1.7 on 2021-03-25 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0019_auto_20210323_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PositionUserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='UserControl.positionlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
