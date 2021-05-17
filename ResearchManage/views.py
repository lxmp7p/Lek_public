from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ResearchFormMKI, MedProductRequestResearchForm, ResearchFormMKIEdit
from .models import MkiFirstRequestResearch, MedProductRequestResearch, MkiFirstRequestResearchHistory, AnotherDocumentsHistory
import datetime
from django.conf.urls.static import static, settings
from .models import User as UserModel
from django.core.files.storage import FileSystemStorage
import random
import os
from func import check_access, logger_func, search
from logger import models as loggerModels
from UserControl import models as UserControlModels
from .functions import *
from django.db import connection
from .models import RequestNumber, ConflictsInterests, logAboutResearch, AnotherDocuments
from django.urls import reverse
import re


check_access = check_access.check_access
now = datetime.datetime.now()


@login_required(login_url='/')
def index(request):
    user = UserModel.objects.filter(username=request.user.username)
    return render(request, "index.html", {'role_id':user[0].role_id,})

@login_required(login_url='/')
def createMkiResearch(request):
    conflictFIOlist = None
    if check_access(5,11,3, user_roleId=request.user.role_id):
        statusSaveRequest = False
        form = ResearchFormMKI(request.POST, request.FILES)  
        if (request.POST):
            if form.is_valid():
                form = form.save(commit=False)
                folderNameTmp = str(form.main_researcher) + "/" + str(form.protocol_number)
                folder_name = setFolderName(folderNameTmp)  #ПЕРЕДАЕМ НЕОБХОДИМЫЙ АРГУМЕНТ КАК НАЗВАНИЕ ПАПКИ
                fileKeys = request.FILES.keys()
                for key in fileKeys:
                    error_message = checkFileSize(request.FILES[key].size)
                    if error_message:
                            return render(request, "MKI/createMkiResearch.html", {
                                                'research_form': form,
                                                'error_message': error_message,})
                for key in fileKeys:
                    temp = saveFile(request, fileKeys, folder_name, key)
                    if temp:
                        conflictFIOlist = temp
                form = editForm(1, request, form)       #ПЕРВЫЙ АРГУМЕНТ ID ТИПА ЗАЯВКИ

                form.save()
                Research = MkiFirstRequestResearch.objects.all().last() 

                saveToHistoryMKI(Research)

                idResearch = Research.id
                typeResearch = Research.type_id
                path = form.main_researcher.FIO + '/' + form.protocol_number
                castResearcherList = re.findall(r'my_cast_researcher_\d*', str(request.FILES))
                for file in castResearcherList:
                    filePath = saveFileThenEditResearch(request.FILES.get(file), path)
                    id_file = re.search('\d+', file).group(0)
                    AnotherDocuments.objects.create(
                        id_research=idResearch,
                        type_research=typeResearch,
                        document=filePath,
                        name_document_id=2,
                        date=request.POST.get('my_cast_researcher_date_' + str(id_file)),
                        version=request.POST.get('my_cast_researcher_ver_' + str(id_file))
                    )

                formInfList = re.findall(r'my_form_inf_\d*', str(request.FILES))
                for file in formInfList:
                    filePath = saveFileThenEditResearch(request.FILES.get(file), path)
                    id_file = re.search('\d+', file).group(0)
                    AnotherDocuments.objects.create(
                        id_research=idResearch,
                        type_research=typeResearch,
                        document=filePath,
                        name_document_id=1,
                        date=request.POST.get('my_form_inf_date_' + str(id_file)),
                        version=request.POST.get('my_form_inf_ver_' + str(id_file)),
                        description=request.POST.get('my_cast_researcher_description_' + str(id_file))
                    )
                RequestNumber.objects.create(id_research = idResearch, type_research = typeResearch)
                saveTeamListInBd(conflictFIOlist, idResearch, typeResearch)
                statusSaveRequest = True
                userList = ConflictsInterests.objects.filter(type_research=typeResearch, id_research=idResearch)
                logAboutResearch.objects.create(condition="Исследование загружено в систему", id_research=Research.id, type_research=Research.type_id, datetime=now.strftime("%Y-%m-%d %H:%M"))
                return redirect('editTeamList', type=typeResearch, id=idResearch)
        form = ResearchFormMKI()                  #МЕНЯЕМ ФОРМУ НА НУЖНУЮ
        return render(request, "MKI/createMkiResearch.html", {'research_form': form, 'statusSaveRequest': statusSaveRequest})
    else:
        return render(request, "index.html")

@login_required(login_url='/')
def editTeamList(request, type, id):
    if check_access(11,2,3,5, user_roleId=request.user.role_id):
        if request.POST:
            idDeleteUsers = request.POST.getlist('deleteUsers')
            newUsers = request.POST.getlist('newUsers')
            if idDeleteUsers:
                for idUser in idDeleteUsers:
                    ConflictsInterests.objects.filter(id=idUser, id_research=id, type_research=type).delete()
            if newUsers:
                for fio in newUsers:
                    ConflictsInterests.objects.create(fio=fio, id_research=id, type_research=type)
            return render(request, "index.html")
        teamList = ConflictsInterests.objects.filter(type_research=type, id_research=id)
        return render(request, "MKI/editTeamList.html", {
            'teamList': teamList,
        })
    else: return render(request, "index.html")

@login_required(login_url='/')
def watchResearchList(request):
    if check_access(11,2,3, user_roleId=request.user.role_id):
        reserchRequestList = MkiFirstRequestResearch.objects.filter(secretar_accepted=False).values_list('id', 'date_created', 'type').union(
                            MedProductRequestResearch.objects.filter(secretar_accepted=False).values_list('id', 'date_created', 'type'))
        logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Просмотрел список исследований')
        return render(request, "watchResearchList.html", {
            'reserchRequestList': reserchRequestList,
        })
    else: return render(request, "index.html")

@login_required(login_url='/')
def watchResearch(request, type, id):
    research_history = logAboutResearch.objects.filter(id_research=id, type_research=type)
    if check_access(11,2,3,5, user_roleId=request.user.role_id):
        if request.POST:
            if 'ACCEPT' in request.POST:
                answerRequestResearch(type=type, id_res=request.POST.get('ACCEPT'), answer='ACCEPT')
                logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Принял исследование(ID=' + str(id) + ')')
            if 'DENIED' in request.POST:
                answerRequestResearch(type=type, id_res=request.POST.get('DENIED'), answer='DENIED')
                logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Отклонил исследование(ID=' + str(id) + ')')
            return redirect("../../../../research/watchResearchList/")
        else: logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Открыл исследование(ID=' + str(id) + ')')
        anotherDocListMki = getLastVersionAnotherFiles(id=id, type=type)
        if (type == 1):
            research = MkiFirstRequestResearch.objects.filter(id=id)
            return render(request, "MKI/watchResearch.html", {
                'research': research,
                'id': id,
                'research_history': research_history,
                'anotherDocListMki':anotherDocListMki,
            })

        if (type == 2):
            research = MedProductRequestResearch.objects.filter(id=id)
            return render(request, "medProduct/watchResearch.html", {
                'research': research,
                'id': id,
            })

    else: return render(request, "index.html")
    return render(request, "index.html")

@login_required(login_url='/')
def getMyResearchsStatus(request):
    research_history = logAboutResearch.objects.all()
    user_access = check_access(11,2,3, user_roleId=request.user.role_id)  #Возвращаем true для пользователя с ролью АДМИНА/Председателя/СЕКРЕТАРЯ
    reserchRequestList = MkiFirstRequestResearch.objects.filter(owner=request.user)
    if request.POST:
        print(request.POST)
        if 'SEARCH' in request.POST:
            reserchRequestList = search.searchResearchList(request.POST.get('SEARCH'))
            return render(request, "myResearchsStatus.html", {
                'reserchRequestList': reserchRequestList,
                'user_access': user_access,
                'research_history': research_history,
            })
    if request.user.role_id == 3: 
         reserchRequestList = MkiFirstRequestResearch.objects.all()
    logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Открыл список своих исследований')
    return render(request, "myResearchsStatus.html", {
                'reserchRequestList': reserchRequestList,
                'user_access': user_access,
                'research_history': research_history,
            })

@login_required(login_url='/')
def editResearch(request, type, id):
    if check_access(11,2,3, user_roleId=request.user.role_id):
        research = MkiFirstRequestResearch.objects.filter(id=id).first()
        research_form = ResearchFormMKIEdit()
        if request.POST:
            editResearchFiles(request, id, type)
        research = MkiFirstRequestResearch.objects.get(id=id)
        saveToHistoryMKI(research)
        return render(request, 'MKI/editResearch.html', {
            'research': research,
            'research_form': research_form,
        })
    else: return render(request, "index.html")

@login_required(login_url='/')
def acceptedResearchsList(request):
    if check_access(11,2,3, user_roleId=request.user.role_id):
        acceptedResearchsList = MkiFirstRequestResearch.objects.filter(secretar_accepted=True, acceptedOnMeeting=True ).values_list('id', 'date_created', 'type', 'acceptedOnMeeting').union(
                            MedProductRequestResearch.objects.filter(secretar_accepted=True, acceptedOnMeeting=True).values_list('id', 'date_created', 'type', 'acceptedOnMeeting'))
        print(acceptedResearchsList)
        logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Открыл список принятых исследований')
        return render(request, "acceptedResearchsList.html", {
            'acceptedResearchsList': acceptedResearchsList,
        })
    else: return render(request, "index.html")


@login_required(login_url='/')
def createMedResearch(request):
    if check_access(5,11, user_roleId=request.user.role_id):
        statusSaveRequest = False
        form = MedProductRequestResearchForm(request.POST, request.FILES)
        if (request.POST):
            if form.is_valid():
                form = form.save(commit=False)
                folder_name = setFolderName(form.id)
                fileKeys = request.FILES.keys()
                for key in fileKeys:
                    error_message = checkFileSize(request.FILES[key].size)
                    if error_message:
                            return render(request, "MKI/createMkiResearch.html", {
                                                'research_form': form,
                                                'error_message': error_message,})
                for key in fileKeys:
                    saveFile(request, fileKeys, folder_name, key)
                form = editForm(2, request, form)
                form.save() 
                statusSaveRequest = True
        form = MedProductRequestResearchForm()  
        return render(request, "medProduct/MedProductRequestResearch.html", 
                                {'research_form': form,
                                'statusSaveRequest': statusSaveRequest,
                                })
    else: return render(request, "index.html")
