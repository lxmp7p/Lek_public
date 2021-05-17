from .models import UserList, Meetings
from UserControl import models as UserModel
from meetingsManage import models as meetingsManageModels
from ResearchManage import models as researchManageModels
import os
import shutil
import datetime
from zipfile import ZipFile
from os import path
from shutil import make_archive
from ResearchManage import models as ResearchModel


now = datetime.datetime.now()


def makeRecordForMeeting(userList, researchList, meeting_id, typeList):
	makeRecordUserList(userList, meeting_id)
	makeRecordResearchList(researchList, meeting_id, typeList)

def makeRecordUserList(userList, meeting_id):
	for userId in userList:
		tmp = UserModel.User.objects.filter(id=userId).first()
		bd = meetingsManageModels.UserList(username=tmp,
                    						meeting_id=meeting_id,)
		bd.save()

def getUserOnId(userList):
	users = []
	for userId in userList:
		return UserModel.User.objects.filter(id=userId).first()

def makeRecordResearchList(researchList, meeting_id, typeList):
	for res in researchList:
		type, id_res = findResearch(typeList)
		del typeList[0]
		if type == '1':
			tmp = researchManageModels.MkiFirstRequestResearch.objects.filter(id=id_res).first().id
			researchManageModels.MkiFirstRequestResearch.objects.filter(id=id_res).update(addedInMeeting=True)
			researchManageModels.logAboutResearch.objects.create(condition='Ваше исследование добавлено в заседание', id_research=id_res, type_research=1, datetime=now.strftime("%Y-%m-%d %H:%M"))
		elif type == '2':
			tmp = researchManageModels.MedProductRequestResearch.objects.filter(id=id_res).first().id
			researchManageModels.MedProductRequestResearch.objects.filter(id=id_res).update(addedInMeeting=True)
			researchManageModels.logAboutResearch.objects.create(condition='Ваше исследование добавлено в заседание', id_research=id_res, type_research=2, datetime=now.strftime("%Y-%m-%d %H:%M"))
		bd = meetingsManageModels.ResearchList(research_id=tmp,
                         						meeting_id=meeting_id,
                         						research_type=type,)
		bd.save()

def findResearch(typeList):
	print(typeList)
	print('--------------------------------------------')
	type = typeList[0][:-(len(typeList[0])-1)]
	id_res = typeList[0][2:]
	return type, id_res

def getResearchOnTypeAndId(type, id):
	if type == '1':
		return researchManageModels.MkiFirstRequestResearch.objects.filter(id=id).first()
	elif type == '2':
		return researchManageModels.MedProductRequestResearch.objects.filter(id=id).first()

def getResearchOnId(id_res, type):
	if type == '1':
		print('dwdwdw')
		return researchManageModels.MkiFirstRequestResearch.objects.filter(id=id_res).first()
	if type == '2':
		return researchManageModels.MedProductRequestResearch.objects.filter(id=id_res).first()

def getResearchInMeeting(meeting_id):
	researchs = meetingsManageModels.ResearchList.objects.filter(meeting_id=meeting_id)
	researchList = []
	try:
		for research in researchs:
			if research.research_type == '1':
				researchList.append(researchManageModels.MkiFirstRequestResearch.objects.filter(id=research.research_id).first())
			if research.research_type == '2':
				researchList.append(researchManageModels.MedProductRequestResearch.objects.filter(id=research.research_id).first())
	except Exception as e:
		researchList = ''
	return researchList

def checkUserInMeeting(user, meeting_id):
	if UserList.objects.filter(username=user, meeting_id=meeting_id):
		return True
	else:
		return False

def getMeetingList(user=None, checkMeetingEnd=None, checkMeetingCreated=None,):
	userListModel = UserList.objects.filter(username=user)
	meetingTemp = checkMeetingList(checkMeetingEnd, checkMeetingCreated)
	meetingList = []
	print(userListModel)
	for user in userListModel:
		print(user)
		for meeting in meetingTemp:
			print(meeting)
			if user.meeting_id == meeting.get('id'):
				meetingList.append(meeting)
	return meetingList

def checkMeetingList(checkMeetingEnd, checkMeetingCreated):
	if (checkMeetingCreated):
		return (Meetings.objects.filter(status='Created').values('id', 'status', 'date', 'time', 'status', 'subpoena'))
	elif (checkMeetingEnd):
		return (Meetings.objects.filter(status='Ended', ).values('id', 'status', 'date', 'time', 'status', 'subpoena'))

def checkUserList(error, positionList, created): 
	userPositionsInMeeting = []
	userMed = False
	userWorker = False
	userSpecialistDoklin = False
	userSpecialist = False
	userNotWorker = False
	print(positionList)
	for userRecords in positionList:
		for record in userRecords:
			if record.position_id == 1 and record.status == 'True':
				userMed = True
			elif record.position_id == 2 and record.status == 'True':
				userSpecialistDoklin = True
			elif record.position_id == 3 and record.status == 'True':
				userWorker = True
			elif record.position_id == 4 and record.status == 'True':
				userSpecialist = True
			elif record.position_id == 3 and record.status == 'False':
				userNotWorker = True
	usersCheck = [userMed, userWorker, userSpecialistDoklin, userSpecialist, userNotWorker]
	print(usersCheck)
	created = True
	for i in usersCheck:
		if i == False:
			if userMed != True:
				error = "В заседании должен участвовать хотя-бы один медик!"
				created = False
			if userWorker != True:
				error = "В заседании должен участвовать хотя-бы один работник!"
				created = False
			if userSpecialistDoklin != True:
				error = "В заседании должен участвовать хотя-бы один специалист доклинических исследований!"
				created = False
			if userSpecialist != True:
				error = "В заседании должен участвовать хотя-бы один специалист клинических исследований!"
				created = False
			if userNotWorker != True:
				error = "Один из участников не должен быть сотрудником учреждения!"
				created = False		
	return error, created

def getConflictWordlist(researchInMeeting, usersInMeeting):
	conflictList = []
	researchConflictInMeeting = []
	for research in researchInMeeting:
		if ResearchModel.ConflictsInterests.objects.filter(id_research=research.id, type_research=research.type_id):
			researchConflictInMeeting.append(ResearchModel.ConflictsInterests.objects.filter(id_research=research.id, type_research=research.type_id))
	for user in usersInMeeting:
		textForCheckType = 'lol'
		if type(user.username) != type(textForCheckType):
			user = user.username
		for listConflict in researchConflictInMeeting:
			for conflict in listConflict:
				fio = str(user.last_name) + ' ' + str(user.first_name) + ' ' + str(user.middle_name)
				if (fio == conflict.fio):
					conflictList.append({'research_id': conflict.id_research, 'research_type': conflict.type_research, 'user': user.username})
	return conflictList


def checkUserInConflictWordlist(conflictList, id_res, type, user):
	conflictHas = True
	countConflict = 0
	for conflict in conflictList:
		if str(conflict.get('research_id')) == str(id_res):
			if str(conflict.get('research_type')) == str(type):
				if str(conflict.get('user')) == str(user):
					conflictHas = False
	return conflictHas

def getMinPeopleForMeeting(request, usersList, researchList):
	usersInMeeting = []
	for user in usersList:
		usersInMeeting.append(getUserOnId([user]))
	researchInMeeting = []
	for research in researchList:
		type_res, id_res = findResearch([research])
		researchInMeeting.append(getResearchOnTypeAndId(type_res, id_res))
	conflictList = getConflictWordlist(researchInMeeting, usersInMeeting)
	conflictCount = [] 
	for research in researchInMeeting:
		for user in usersInMeeting:
			if not checkUserInConflictWordlist(conflictList, research.id, research.type_id, user):
				conflictCount.append({'research_id': research.id})
	countIdConflict = []
	for conflict in conflictCount:
		countIdConflict.append(conflict.get('research_id'))
	max = 0
	for id_res in countIdConflict:
		count = 0
		for idToCheck in countIdConflict:
			if id_res == idToCheck:
				count += 1
		if count > max:
			max = count
	return max

def getInfoList():
	wordlist = [
		'Для создания заседания необходимо выбрать как минимум 5 участников без конфликта интересов ',
		'Для создания заседания необходимо выбрать как минимум 1 исследование',
		'Один из участников не должен быть сотрудником учреждения',
		'В заседании должен участвовать хотя-бы один медик',
		'В заседании должен участвовать хотя-бы один специалист доклинических исследований',
		'В заседании должен участвовать хотя-бы один специалист клинических исследований',
		'Один из участников не должен быть сотрудником учреждения',
		]
	return wordlist

def getUserCheck():
	return 'Для создания заседания необходимо выбрать как минимум 5 участников без конфликта интересов'

def getResearchCheck():
	return 'Для создания заседания необходимо выбрать как минимум 1 исследование'

def workerCheck():
	return 'Один из участников не должен быть сотрудником учреждения'

def medikCheck():
	return 'В заседании должен участвовать хотя-бы один медик'

def specDICheck():
	return 'В заседании должен участвовать хотя-бы один специалист доклинических исследований'

def specKI():
	return "В заседании должен участвовать хотя-бы один специалист клинических исследований"

def notWorker():
	return 'Один из участников не должен быть сотрудником учреждения!'

