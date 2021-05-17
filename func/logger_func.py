from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf.urls.static import static, settings
from ResearchManage import models as ResearchModel
from UserControl import models as UserModel
from logger import models as loggerModels

def setInfoInLogger(user, datetime, action):
	loggerModels.LoggerRecords.objects.create(
		user=user,
		datetime=datetime, 
		action=action,
		username=user.username)
	print(user.username)	


