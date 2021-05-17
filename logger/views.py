from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from func import check_access
from .models import LoggerRecords
from func import check_access, search
from UserControl import models as UserModel

check_access = check_access.check_access


@login_required(login_url='/')
def records(request):
	'''
	if check_access(11,2,3, user_roleId=request.user.role_id):
		if request.POST:
			if 'SEARCH' in request.POST:
				bd = search.searchUsernameInLogger(request.POST.get('SEARCH'))
				return render(request, 'logger/records.html', {'bd': bd,})
		bd = LoggerRecords.objects.all().values('username',  'datetime', 'action')
		print(bd[0])
		return render(request, 'logger/records.html', {'bd': bd,})
	return render(request, 'index.html')
	'''