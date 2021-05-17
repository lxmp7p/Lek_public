from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from .views import ethicalStandard

urlpatterns = [
	path('', ethicalStandard,  name='ethicalStandard'),
]
