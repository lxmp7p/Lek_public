from .models import *
from docxtpl import DocxTemplate
import datetime
from django.core.files.storage import FileSystemStorage
import random
from ResearchManage import models as ResearchManageModel
import os
import zipfile
from django.conf.urls.static import static, settings
from django.db import connection
import re
from django.http import QueryDict


now = datetime.datetime.now()


def saveZipInBd(folder_name, multipleFileList):
	zipFile = str(folder_name) + '/' + str(multipleFileList[0]) + '.zip'
	record = MkiFirstRequestResearch.objects.filter().last()
	MkiFirstRequestResearch.objects.filter(id=record.id).update(cast_researcher=zipFile)

	zipFile = str(folder_name) + '/' + str(multipleFileList[1]) + '.zip'
	record = MkiFirstRequestResearch.objects.filter().last()
	MkiFirstRequestResearch.objects.filter(id=record.id).update(form_inf=zipFile)

def editResearchFiles(request, id, type):
	model = getTypeForSql(type)
	#tmp = {k: v for k, v in request.POST if v}
	postDict = dict(request.POST)
	tmpDict = {'csrfmiddlewaretoken': postDict.get('csrfmiddlewaretoken')}
	for key in postDict:
		if (postDict.get(key) != ['']):
			tmpDict.update({key:postDict.get(key)})
	query_dict = QueryDict('', mutable=True)
	query_dict.update(tmpDict)
	listKeys = [*query_dict.keys(), *request.FILES.keys(),]
	formInfList = re.findall(r'my_form_inf_\d*', str(request.FILES))
	if (type == 1):
		researchInModel = MkiFirstRequestResearch.objects.get(id=id, type_id = type)
		path = researchInModel.main_researcher.FIO + '/' + researchInModel.protocol_number
	if formInfList:
		AnotherDocuments.objects.filter(
			id_research=id,
			type_research=type).delete()

		for file in formInfList:
			filePath = saveFileThenEditResearch(request.FILES.get(file), path)
			id_file = re.search('\d+', file).group(0)
			AnotherDocuments.objects.create(
            id_research=id,
            type_research=type,
            document=filePath,
            name_document_id=1,
            date=request.POST.get('my_form_inf_date_' + str(id_file)),
            version=request.POST.get('my_form_inf_ver_' + str(id_file)),
            description=request.POST.get('my_form_inf_description_' + str(id_file))
      	)
			recordForHistory = AnotherDocuments.objects.all().last()
			saveToHistoryAnotherFiles(recordForHistory)
	castResearcherList = re.findall(r'my_cast_researcher_\d*', str(request.FILES))
	if castResearcherList:
		for file in castResearcherList:
			print(request.FILES)
			filePath = saveFileThenEditResearch(request.FILES.get(file), path)
			id_file = re.search('\d+', file).group(0)
			AnotherDocuments.objects.create(
			   id_research=id,
			   type_research=type,
			   document=filePath,
			   name_document_id=2,
			   date=request.POST.get('my_cast_researcher_date_' + str(id_file)),
			   version=request.POST.get('my_cast_researcher_ver_' + str(id_file)),
			   description=request.POST.get('my_cast_researcher_description_' + str(id_file)),

			)
			recordForHistory = AnotherDocuments.objects.all().last()
			saveToHistoryAnotherFiles(recordForHistory)
	for key in listKeys:
		if re.findall(r'my_form_inf_\d*', key) or re.findall(r'my_cast_researcher_\d*', key):
			break
		if key not in request.FILES.keys():
			change = request.POST.get(key)
		if request.FILES.get(key):
			change = saveFileThenEditResearch(request.FILES.get(key), path)
			print(request.FILES.get(key))
		else:
			pass
		if (key == 'csrfmiddlewaretoken'):
			continue
		with connection.cursor() as cursor:
			cursor.execute("""
				UPDATE """ + str(model) + """
				SET """ + str(key) + """=%s
				WHERE id=%s
				""", [change, id])
	return True

def getTypeForSql(type):
	if(type==1):
		return 'MkiFirstRequestResearch '


def saveFileThenEditResearch(myfile, folder_name_tmp):
	folder_name = setFolderName(folder_name_tmp)
	fs = FileSystemStorage()
	fs.base_location = fs.base_location + folder_name
	fs.base_location = getValidPath(fs.base_location)
	filename = fs.save(myfile.name, myfile)
	path = folder_name + filename
	return path

def saveFile(request, fileKeys, folder_name, key):
	conflictFIOlist = None
	myfile = request.FILES[key]
	fs = FileSystemStorage()
	fs.base_location = fs.base_location + folder_name
	fs.base_location = getValidPath(fs.base_location)
	filename = fs.save(myfile.name, myfile)
	if (key == 'list_members'):
		conflictFIOlist = getUserListOnTeamList(str(fs.base_location) + '/' + str(filename))
	#logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Загрузил файлы в систему')
	if conflictFIOlist:
		return conflictFIOlist
	else:
		return False

def getUserListOnTeamList(document):
	userList = ['Ошибка автоматического определения. Заполните поля.']
	try:
		doc = DocxTemplate(document)
		row = 2
		userList = []
		while True:
			fio = doc.tables[0].cell(row, 1).text.replace('\n', ' ')
			fio = fio.replace('  ', ' ')
			userList.append(fio)
			row += 1
	except Exception as e:
		print('Error' + str(e))
	return userList

def saveTeamListInBd(teamList, id, type):
	if teamList:
		for fio in teamList:
			if not ConflictsInterests.objects.filter(fio=fio, id_research=id, type_research=type):
				ConflictsInterests.objects.create(fio=fio, id_research=id, type_research=type)


def checkFileSize(size):
	if size > 1024 * 1024 * 250:
		error_message =  'Загружен слишком большой файл!'
		logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Пытался загрузить файл размером ' + str(size/1024/1024) + 'MB')
		return error_message
	else:
		return False


# не работает
def checkFileType(path):
	acceptedExtension = ['zip', 'docx', 'doc', 'img', 'jpg', 'jpeg', 'zip', 'rar' ]
	extension = path.split('.')[-1]
	for i in acceptedExtension:
		if i != extension:
			error_message = 'Загружен неверный файл!'
			logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Пытался загрузить файл с расширением: ' + str(extension))
			return error_message
	else:
		return False

def setFolderName(folder_name):
	folder_name =  '/request_researchs/' + str(now.strftime("%Y")) + '/' + str(folder_name) +  '/' + str(now.strftime("%d-%m"))
	return folder_name

def editForm(type, request, form):
	form.owner = request.user
	form.type_id = type
	form.date_created = now.strftime("%d-%m-%Y %H:%M")
	form.secretar_accepted = False
	if request.user.role_id == 3:
		form.secretar_accepted = True
		form.secretar_accepted_date = now

	form.status = 'False'
	return form


def answerRequestResearch(type, id_res, answer):
	if (type == 1):
		requestResearchManager(ResearchManageModel.MkiFirstRequestResearch, answer, id_res)
	if (type == 2):
		requestResearchManager(ResearchManageModel.MedProductRequestResearch, answer, id_res)

def requestResearchManager(model, answer, id_res):
	if (answer == 'ACCEPT'):
		model.objects.filter(id=id_res).update(secretar_accepted=True, secretar_accepted_date=now)
	elif (answer == 'DENIED'):
		model.objects.filter(id=id_res).delete()

def getValidPath(path):
	return re.sub('[!@#$*]', '', path)

def saveToHistoryMKI(research):
	ver = getLastResearchVersion(research)
	MkiFirstRequestResearchHistory.objects.create(	
		subpoena = research.subpoena,
		addedInMeeting = research.addedInMeeting,
		report = research.report,
		acceptedOnMeeting = research.acceptedOnMeeting,
		protocol_number = research.protocol_number,
		description = research.description,
		secretar_accepted = research.secretar_accepted,
		secretar_accepted_date = research.secretar_accepted_date,
		date_created = research.date_created,
		document = research.document,
		status = research.status,
		list_members = research.list_members,
		ver_bio = research.ver_bio,
		accept_research = research.accept_research,
		accept_research_version = research.accept_research_version,
		accept_research_date = research.accept_research_date,
		protocol_research = research.protocol_research,
		protocol_research_version = research.protocol_research_version,
		protocol_research_date = research.protocol_research_date,
		contract = research.contract,
		contract_date = research.contract_date,
		advertising = research.advertising,
		write_objects = research.write_objects,
		name_another_doc = research.name_another_doc,
		another_doc = research.another_doc,
		another_doc_version = research.another_doc_version,
		another_doc_date = research.another_doc_date,
		type = research.type,
		owner = research.owner,
		main_researcher = research.main_researcher,
		expert = research.expert,
		datetime_edit = now.strftime("%Y-%m-%d %H:%M"),
		research = research,
		ver=ver,
	)

def saveToHistoryAnotherFiles(record):
	ver=1
	print(record)
	if AnotherDocumentsHistory.objects.filter(id_research=record.id_research):
		lastEdit = AnotherDocumentsHistory.objects.filter(id_research=record.id_research).last()
		ver = lastEdit.ver + 1
	AnotherDocumentsHistory.objects.create(
		id_research=record.id_research,
		type_research=record.type_research,
		document=record.document,
		name_document_id=record.name_document_id,
		version=record.version,
		date=record.date,
		ver=ver,
	)

def getLastResearchVersion(research):
	ver = 1
	if MkiFirstRequestResearchHistory.objects.filter(research_id=research.id):
		lastEdit = MkiFirstRequestResearchHistory.objects.filter(research_id=research.id).last()
		ver = lastEdit.ver + 1
	return ver

def getLastVersionAnotherFiles(id=None, type=None):
	anotherDocListMki = []
	if AnotherDocuments.objects.filter(id_research = id,type_research = type):
		anotherDocListMki.append(AnotherDocuments.objects.filter(
			id_research = id,
			type_research = type,
		))
	return anotherDocListMki