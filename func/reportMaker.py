from docxtpl import DocxTemplate
import datetime
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive
from ResearchManage import models as ResearchModel
from meetingsManage import models as MeetingModels
import docx
import zipfile
from django.core.files.storage import FileSystemStorage
import shutil


now = datetime.datetime.now()


def makeEndMeetingReport(id, type, research, userList, dateMeeting, time, acceptedCount, deniedCount, dontVoited, protocolDescription, verdict, meeting_id):
	documentListText = makeDocList(research, type)
	doc = DocxTemplate("media/шаблон.docx" )
	expert = ''
	print(research.expert)
	if research.expert:
		expert = str(research.expert.last_name) + ' ' + str(research.expert.first_name[:1])  + '.' + str(research.expert.middle_name[:1]) + '.',
		expert = str(expert[0])
	context = {'userList': userList, 
				'date': dateMeeting.strftime("%d.%m.%Y"),
				'time': time,
				'docsList': documentListText,
				'acceptedCount': acceptedCount,
				'deniedCount': deniedCount,
				'dontVoited': dontVoited,
				'protocolDescription': protocolDescription,
				'verdict': verdict, 
				'dateY': dateMeeting.year,
				'id': id,
				'expert': expert,
				}
	doc.render(context)
	path = 'media/reports/Выписки/id=' + str(meeting_id)
	pathFix = 'reports/Выписки/id=' + str(meeting_id)
	try:
		os.mkdir(path)
	except:
		pass
	pathToSave = pathFix + '/' + str(id) + '-' + now.strftime("%d-%m-%Y") + ".docx"
	doc.save(path + '/' + str(id) + '-' + now.strftime("%d-%m-%Y") + ".docx")
	if type == 1:
		ResearchModel.MkiFirstRequestResearch.objects.filter(id=id).update(report=pathToSave)
	return 

def makeSubpoena(id, type, research, dateMeeting, time, protocolDescription, meeting_id):
	documentListText = makeDocList(research, type)
	doc = DocxTemplate("media/шаблон повестки.docx")
	context = {
				'date': dateMeeting.strftime("%d.%m.%Y"),
				'time': time,
				'protocolDescription': protocolDescription,
				'main_researcher': research.main_researcher,
				'protocol_number': research.protocol_number,
				'docsList': documentListText,
				'id_research': research.id,
				'date_created': research.date_created,
				'id_meeting': id,
				'owner_info': f"{research.owner.last_name} {research.owner.first_name} {research.owner.middle_name}, {research.owner.phone_number} {research.owner.email}"
				}
	doc.render(context)
	path = 'media/reports/Повестки/id=' + str(meeting_id)
	pathFix = 'reports/Повестки/id=' + str(meeting_id)
	try:
		os.mkdir(path)
	except:
		pass
	pathToSave = pathFix + '/' + str(id) + '-' + now.strftime("%d-%m-%Y") + ".docx"
	doc.save(path + '/' + str(id) + '-' + now.strftime("%d-%m-%Y") + ".docx")
	return path

def saveSubpoenaOnZip(meeting_id, path, ):
	shutil.make_archive('media/reports/Повестки/id=' + str(meeting_id) ,
                    'zip',
                    'media/reports/Повестки',
                    'id=' + str(meeting_id))
	MeetingModels.Meetings.objects.filter(id=meeting_id).update(subpoena=path+'.zip')

def makeDocList(research, type):
	if (type == 1):
		anotherDocuments = ResearchModel.AnotherDocuments.objects.filter(id_research=research.id, type_research=type)
		acceptResearch = None
		acceptForm = ''
		if research.accept_research_date:
			acceptResearch = '\nРазрешение МЗ РФ №' + str(research.accept_research_version) + ' на проведение клинического исследования *, от : ' + str(research.accept_research_date.strftime("%d.%m.%Y")) + '\n'
#		if research.form_inf_date:
#			acceptForm = 'Форма информированного листа, версия: ' + str(research.form_inf_version) + ', дата: ' + str(research.form_inf_date.strftime("%d.%m.%Y")) + '\n'
		documentListText = ('Направительное письмо в МЗ РФ для получения разрешения на проведение клинического исследования ' + str(research.protocol_number) + 'от * 2021 г.\n' +
							'Протокол клинического исследования. Лекарственный препарат: * . Код проекта: ' + str(research.protocol_number) +'.Редакция номер: '+ str(research.protocol_research_version) + ', дата: ' + str(research.protocol_research_date.strftime("%d.%m.%Y")) + '\n' +
							'Копия договора обязательного страхования жизни и здоровья пациентов, участвующих в клиническом исследовании лекарственного препарата * , от: ' + str(research.contract_date))
		if (anotherDocuments):
			for doc in anotherDocuments:
				if (doc.name_document_id == 1):
					documentListText += '\nИнформационный листок пациента ' + str(doc.description) + ' версии: ' + str(doc.version) + ' от: ' + str(doc.date)
				if (doc.name_document_id == 2):
					documentListText += '\nБрошюра исследователя по препарату * номер издания: ' + str(doc.version) + ' от: ' + str(doc.date) + ' ' + str(doc.description)
		if (acceptResearch):
			documentListText += acceptResearch
		if (acceptResearch):
			documentListText += acceptForm
		if (research.advertising):
			documentListText += 'Образцы рекламной продукции \n'
		if (research.write_objects):
			documentListText += 'Письменные материалы'
		if (research.name_another_doc):
			documentListText += str(research.name_another_doc)
			if (research.another_doc_version):
				documentListText += ', версия: ' + str(research.another_doc_version)
			if(research.another_doc_date):
				documentListText += ', дата: ' + str(research.another_doc_date)	
	return (documentListText)
