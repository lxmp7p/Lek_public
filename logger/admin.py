from django.contrib import admin

# Register your models here.
from .models import LoggerRecords

@admin.register(LoggerRecords)
class LoggerRecordsAdmin(admin.ModelAdmin):
	search_fields = ("username__startswith", )
	list_display = ("username", "datetime", 'action')