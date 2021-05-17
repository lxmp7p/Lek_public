# Generated by Django 3.1.7 on 2021-05-13 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('UserControl', '0030_auto_20210513_1343'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ResearchManage', '0048_auto_20210513_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMkiFirstRequestResearch',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('subpoena', models.TextField(max_length=100)),
                ('addedInMeeting', models.BooleanField(default=False)),
                ('report', models.TextField(max_length=100)),
                ('acceptedOnMeeting', models.CharField(max_length=20)),
                ('protocol_number', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('secretar_accepted', models.CharField(max_length=10)),
                ('secretar_accepted_date', models.DateField(blank=True, null=True)),
                ('date_created', models.CharField(max_length=50)),
                ('document', models.TextField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('list_members', models.TextField(max_length=100)),
                ('ver_bio', models.CharField(max_length=50)),
                ('accept_research', models.TextField(blank=True, max_length=100, null=True)),
                ('accept_research_version', models.CharField(blank=True, max_length=50, null=True)),
                ('accept_research_date', models.DateField(blank=True, null=True)),
                ('protocol_research', models.TextField(max_length=100)),
                ('protocol_research_version', models.CharField(max_length=50)),
                ('protocol_research_date', models.DateField()),
                ('contract', models.TextField(max_length=100)),
                ('contract_date', models.DateField()),
                ('advertising', models.TextField(blank=True, max_length=100, null=True)),
                ('write_objects', models.TextField(blank=True, max_length=100, null=True)),
                ('name_another_doc', models.CharField(blank=True, max_length=50, null=True)),
                ('another_doc', models.TextField(blank=True, max_length=100, null=True)),
                ('another_doc_version', models.CharField(blank=True, max_length=50, null=True)),
                ('another_doc_date', models.DateField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('expert', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('main_researcher', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='UserControl.pi_birthday')),
                ('owner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ResearchManage.requestsresearchslist')),
            ],
            options={
                'verbose_name': 'historical mki first request research',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]