from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime
from django.conf.urls.static import static, settings
from ResearchManage import models as ResearchModel
from UserControl import models as UserModel
from .models import Meetings
from .models import ResearchList
from .models import UserList
from .models import VoteList
from .models import ExpertRequest
from .forms import MeetingForm
from func import check_access, reportMaker, logger_func
from logger import models as loggerModels
from .functions import *
import re



now = datetime.datetime.now()
check_access = check_access.check_access


def checkConflict(request):
    researchListMki = ResearchModel.MkiFirstRequestResearch.objects.filter(secretar_accepted=True, addedInMeeting=False)
    researchListMed = ResearchModel.MedProductRequestResearch.objects.filter(secretar_accepted=True, addedInMeeting=False)
    userList = UserModel.User.objects.filter(registration_accepted=True, docStatus='True')
    researchLists = None
    userList = None
    if request.method == 'GET':
        print(request.GET.getlist('userList[]'))
        form = MeetingForm(request.GET)
        researchLists = request.GET.getlist('researchLists[]')
        userList = request.GET.getlist('userList[]')
        max = getMinPeopleForMeeting(request, userList, researchLists)
        minCount = len(userList)
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        researchLists = request.POST.getlist('researchLists[]')
        userList = request.POST.getlist('userList[]')
        max = getMinPeopleForMeeting(request, userList, researchLists)
        minCount = len(userList)
    infoList = []
    if minCount < 5 + max:
        infoList.append(getUserCheck())
    if not researchLists:
        infoList.append(getResearchCheck())
    record = None
    userMed = False
    userWorker = False
    userSpecialistDoklin = False
    userSpecialist = False
    userNotWorker = False

    for user_id in userList:
        recordList = UserModel.PositionUserList.objects.filter(user_id=user_id)
        for record in recordList:
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
    for i in usersCheck:
        if i == False:
            if userMed != True:
                infoList.append(medikCheck())
            if userWorker != True:
                infoList.append(workerCheck())
            if userSpecialistDoklin != True:
                infoList.append(specDICheck())
            if userSpecialist != True:
                infoList.append(specKI())
            if userNotWorker != True:
                infoList.append(notWorker())

    if infoList == []:
        infoList = None

    return render(request, "meeting/createMeeting.html", {
                            'researchListMki': researchListMki,
                            'researchListMed': researchListMed,
                            'userList': userList,
                            'form': MeetingForm,
                            'infoList': infoList,
                            })

@login_required(login_url='/')
def createMeeting(request):
    """
    Создание собрания
    """
    infoList = getInfoList()
    dateMin = datetime.datetime.strptime(now.strftime("%Y-%m-%d"), "%Y-%m-%d")
    dateMin += datetime.timedelta(days=3)
    created = ''
    researchListMki = ResearchModel.MkiFirstRequestResearch.objects.filter(secretar_accepted=True, addedInMeeting=False)
    researchListMed = ResearchModel.MedProductRequestResearch.objects.filter(secretar_accepted=True, addedInMeeting=False)
    userList = UserModel.User.objects.filter(registration_accepted=True, docStatus='True')
    if check_access(11,2,3, user_roleId=request.user.role_id):
        if request.method == 'POST':
            if 'userCreateMeetingBtn' in request.POST:
                print(request.POST)
                error = ''
                form = MeetingForm(request.POST)
            
                if form.is_valid():
                    form = form.save(commit=False)
                    form.status = False
                    if form.date < dateMin.date():
                        error = 'Неверная дата!'
                        return render(request, "meeting/createMeeting.html", {
                                            'researchListMki': researchListMki,
                                            'researchListMed': researchListMed,
                                            'userList': userList,
                                            'form': MeetingForm,
                                            'error': error,
                                    })

                    form.save()
                    bd = Meetings.objects.all().last()
                    try:
                        id = bd.id
                    except Exception as e:
                        error = "Неизвестная ошибка!"
                        return render(request, "meeting/createMeeting.html", {
                            'researchListMki': researchListMki,
                            'researchListMed': researchListMed,
                            'userList': userList,
                            'form': MeetingForm,
                            'error': error,
                        })

                    max = getMinPeopleForMeeting(request, request.POST.getlist('usersListType'), request.POST.getlist('researchListsType'))
                    minCount = len(request.POST.getlist('userLists')) - max


                    if minCount < 5 + max:
                        error = "Для создания заседания необходимо выбрать как минимум 5 участников без конфликта интересов!"
                        return render(request, "meeting/createMeeting.html", {
                        'researchListMki': researchListMki,
                        'researchListMed': researchListMed,
                        'userList': userList,
                        'form': MeetingForm,
                        'error': error,
                    })


                    if len(request.POST.getlist('researchLists')) < 1:
                        error = "Для создания заседания необходимо выбрать как минимум 1 исследование!"
                        return render(request, "meeting/createMeeting.html", {
                        'researchListMki': researchListMki,
                        'researchListMed': researchListMed,
                        'userList': userList,
                        'form': MeetingForm,
                        'error': error,
                    })
                    positionList = []
                    man = 0
                    woman = 0
                    for userId in request.POST.getlist('usersListType'):
                        user = UserModel.User.objects.filter(id=userId).first()
                        positionList.append(UserModel.PositionUserList.objects.filter(user=user))
                        if (user.sex == "Man"):
                            man += 1
                        if (user.sex == "Woman"):
                            woman += 1
                    if (man == len(request.POST.getlist('userLists')) or woman == len(request.POST.getlist('userLists'))):
                        error = "В заседании не могут участвовать эксперты только одного пола!"
                        return render(request, "meeting/createMeeting.html", {
                            'researchListMki': researchListMki,
                            'researchListMed': researchListMed,
                            'userList': userList,
                            'form': MeetingForm,
                            'error': error,
                    })
                    error, created = checkUserList(error, positionList, created)
                    if error == '':
                        meeting = Meetings.objects.all().last()
                        Meetings.objects.filter(id=meeting.id).update(status='Created')
                        Meetings.objects.filter(status='False').delete()
                        Meetings.objects.filter(status='False').delete()

                    if created:
                        userListReq = request.POST.getlist('usersListType')
                        typeList = request.POST.getlist('researchListsType')
                        researchListReq = request.POST.getlist('researchLists')
                        makeRecordForMeeting(userListReq, researchListReq, id, typeList)
                        meeting = Meetings.objects.all().last()
                        researchInMeeting = getResearchInMeeting(meeting_id=meeting.id)
                        path = ''
                        for research in researchInMeeting:
                            path = reportMaker.makeSubpoena(id = research.id,
                                type = research.type_id,
                                research = research,
                                dateMeeting = meeting.date, 
                                time = meeting.time, 
                                protocolDescription = research.description,
                                meeting_id = meeting.id,
                            )
                        reportMaker.saveSubpoenaOnZip(meeting.id, path)
                        meeting = Meetings.objects.all().last()
                        print(meeting.date)
                        return render(request, "meeting/createMeeting.html", {
                                            'researchListMki': researchListMki,
                                            'researchListMed': researchListMed,
                                            'userList': userList,
                                            'form': MeetingForm,
                                            'created': created,
                                        })
                    else:
                        return render(request, "meeting/createMeeting.html", {
                                            'researchListMki': researchListMki,
                                            'researchListMed': researchListMed,
                                            'userList': userList,
                                            'form': MeetingForm,
                                            'error': error,
                                    })
               
                    #logger_func.setInfoInLogger(user=request.user, ip=request.META.get('REMOTE_ADDR'), datetime=now.strftime("%d-%m-%Y %H:%M"), action='Создание собрания')
        return render(request, "meeting/createMeeting.html", {
                                            'researchListMki': researchListMki,
                                            'researchListMed': researchListMed,
                                            'userList': userList,
                                            'form': MeetingForm,
                                            'dateMin': dateMin,
                                            'infoList': infoList,
                                    })
    else: return render(request, "index.html")

@login_required(login_url='/')
def watchMeeting(request):
    """
    Просмотр списка собраний
    """
    if check_access(11,1,2,3,4,6,7,8,9,10, user_roleId=request.user.role_id):
        meetingList = getMeetingList(user=request.user, checkMeetingCreated=True)
        logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Открыл список собраний')
        return render(request, "meeting/watchMeeting.html", {
                      'meetingList': meetingList,
        })
    else: return render(request, "index.html")


@login_required(login_url='/')
def watchMeetingEnded(request):
    """
    Просмотр списка собраний
    """
    if check_access(11,1,2,3,4,6,7,8,9,10, user_roleId=request.user.role_id):
        meetingList = getMeetingList(user=request.user, checkMeetingEnd=True)
        logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Открыл список собраний')
        return render(request, "meeting/watchMeeting.html", {
                      'meetingList': meetingList,
                      'ended': True,
        })
    else: return render(request, "index.html")

@login_required(login_url='/')
def openMeeting(request, id):
    '''
    The function allows you to open meeting, set your voice and end meeting.
    Then you set your vote, function check in model has your on another status
    if True func update status and set this in model.
    Also func count vote and has method was end meeting and set him status
    Ended and save report on all research result in this meeting.
    '''

    if check_access(11,1,2,3,4,6,7,8,9,10, user_roleId=request.user.role_id):
        if (checkUserInMeeting(request.user, id)):
            RequestNumberList = ResearchModel.RequestNumber.objects.all()
            acceptToAdminSetting = check_access(11,2,3, user_roleId=request.user.role_id)
            meetingCheckStatus = Meetings.objects.filter(id=id).first()
            usersInMeeting = UserList.objects.filter(meeting_id=id)
            researchInMeeting = getResearchInMeeting(meeting_id=id)

            conflictList = getConflictWordlist(researchInMeeting, usersInMeeting)
            
            vCount = VoteList.objects.filter(meeting_id=id)
            temp = []
            usersAcceptedList = []
            usersDeniedList = []
            for i in vCount:
                if VoteList.objects.filter(id=i.id, type_res=i.type_res, status='ACCEPT'):
                    usersAcceptedList.append(VoteList.objects.filter(id=i.id, type_res=i.type_res, status='ACCEPT').first())
                if VoteList.objects.filter(id=i.id, type_res=i.type_res, status='DENIED'):
                    usersDeniedList.append(VoteList.objects.filter(id=i.id, type_res=i.type_res, status='DENIED').first())
            timeForWrite = now.strftime("%d-%m-%Y %H:%M")
            if request.POST:
                secretar_id_form_request =  re.search(r'SET_SECRETAR\d*', str(request.POST))
                if secretar_id_form_request:
                    secretar_id_form_request = secretar_id_form_request.group(0).replace('SET_SECRETAR', '')
                if request.POST.get('TYPE') == 'ACCEPT':
                    post_req = request.POST['RESEARCH']
                    message = request.POST['MESSAGE']
                    type = post_req[:-(len(post_req)-1)]
                    id_res = post_req[2:]
                    if checkUserInConflictWordlist(conflictList, id_res, type, request.user):
                        if not VoteList.objects.filter(username_vote=request.user, type_res=type, meeting_id=id,research_id=getResearchOnId(id_res, type).id):
                            VoteList.objects.create(username_vote=request.user,
                                                status='ACCEPT',
                                                meeting_id=id,
                                                type_res=type,
                                                datetime=timeForWrite,
                                                message=message,
                                                research_id=getResearchOnId(id_res, type).id)
                        else:
                            VoteList.objects.filter(username_vote=request.user,
                                                meeting_id=id,
                                                type_res=type,
                                                research_id=getResearchOnId(id_res, type).id).update(status='ACCEPT', message=message, datetime=timeForWrite,)
                if request.POST.get('TYPE') == 'DENIED':
                    post_req = request.POST['RESEARCH']
                    message = request.POST['MESSAGE']
                    type = post_req[:-(len(post_req)-1)]
                    id_res = post_req[2:]
                    if checkUserInConflictWordlist(conflictList, id_res, type, request.user):
                        if not VoteList.objects.filter(username_vote=request.user, type_res=type, meeting_id=id,research_id=getResearchOnId(id_res, type).id):
                            VoteList.objects.create(username_vote=request.user,
                                                status='DENIED',
                                                meeting_id=id,
                                                type_res=type,
                                                datetime=timeForWrite,
                                                message=message,
                                                research_id=getResearchOnId(id_res, type).id)
                        else:
                            VoteList.objects.filter(username_vote=request.user,
                                                meeting_id=id,
                                                type_res=type,
                                                research_id=getResearchOnId(id_res, type).id).update(status='DENIED', message=message, datetime=timeForWrite,)
                elif 'EXPERT' in request.POST:
                    id_type, id_research = request.POST.get('EXPERT').split('.')
                    if (id_type == '1'):
                        research = ResearchModel.MkiFirstRequestResearch.objects.filter(id=id_research).first()
                        user = request.user
                    if ExpertRequest.objects.filter(research=research, user_expert=user):
                        ExpertRequest.objects.filter(research=research, user_expert=user).delete()
                    ExpertRequest.objects.create(research=research, user_expert=user)


                elif 'END_MEETING' in request.POST:
                    reportVoiceList = VoteList.objects.filter(meeting_id=id)
                    reportResearchList = []
                    for i in reportVoiceList:
                        for j in reportVoiceList:
                            if (i.research_id == j.research_id):
                                reportResearchList.append(j.research_id)
                    reportResearchList = set(reportResearchList)

                    users = UserList.objects.filter(meeting_id=id)
                    userListReport = ''
                    for user in users:
                        userListReport += (user.username.last_name + ' ' + 
                        user.username.first_name[0] + '.' + 
                        user.username.middle_name[0] + '. - ' +
                        user.username.role.name + '\n')
                    meeting = Meetings.objects.filter(id=id)
                    for research in researchInMeeting:
                        deniedCount = len(VoteList.objects.filter(research_id = research.id, status = 'DENIED'))
                        acceptedCount = len(VoteList.objects.filter(research_id = research.id, status = 'ACCEPT'))
                        verdict = ''
                        if (deniedCount > acceptedCount):
                            verdict = 'Отклонить '
                            if research.type_id == 1:
                                ResearchModel.MkiFirstRequestResearch.objects.filter(id=research.id).update(acceptedOnMeeting='False')
                                ResearchModel.logAboutResearch.objects.create(condition="Исследование отклонено на заседании", id_research=Research.id, type_research=Research.type_id, datetime=now.strftime("%Y-%m-%d %H:%M"))
                        if (deniedCount < acceptedCount):
                            verdict = 'Одобрить '
                            if research.type_id == 1:
                                ResearchModel.MkiFirstRequestResearch.objects.filter(id=research.id).update(acceptedOnMeeting='True')
                                ResearchModel.logAboutResearch.objects.create(condition="Исследование одобрено на заседании", id_research=research.id, type_research=research.type_id, datetime=now.strftime("%Y-%m-%d %H:%M"))

                        reportMaker.makeEndMeetingReport(
                            id = research.id,
                            type = research.type_id,
                            research = research,
                            userList = userListReport,
                            dateMeeting = meeting[0].date, 
                            time = meeting[0].time, 
                            acceptedCount = acceptedCount,
                            deniedCount = deniedCount,
                            dontVoited = len(users) - len(VoteList.objects.filter(research_id = research.id, status = 'ACCEPT')) - len(VoteList.objects.filter(research_id = research.id, status = 'DENIED')),
                            protocolDescription = research.description,
                            verdict = verdict,
                            meeting_id = id,
                        )
                    Meetings.objects.filter(id=id).update(status='Ended')
                    return render(request, "index.html")
                elif request.POST.getlist('SET_SECRETAR' + secretar_id_form_request):
                    if request.POST.getlist('SET_SECRETAR' + secretar_id_form_request) != ['', '', ''] or str(request.POST.get('SET_SECRETAR' + secretar_id_form_request)) != 'None':
                        id_type = request.POST.getlist('SET_SECRETAR_TYPE' + secretar_id_form_request)[0]
                        id_research =  request.POST.getlist('SET_SECRETAR' + secretar_id_form_request)[0]
                        id_user = request.POST.getlist('SET_SECRETAR_USER' + secretar_id_form_request)[0]
                        if (id_type == '1'):
                            model = ResearchModel.MkiFirstRequestResearch
                            research = ResearchModel.MkiFirstRequestResearch.objects.filter(id=id_research).first()
                            user = UserModel.User.objects.filter(id=id_user).first()
                        model.objects.filter(id=id_research).update(expert=user)

            type_id = researchInMeeting[0].type_id

            anotherDocListMki = []
            for research in researchInMeeting:
                if ResearchModel.AnotherDocuments.objects.filter(id_research = research.id,type_research = research.type_id,):
                    anotherDocListMki.append(ResearchModel.AnotherDocuments.objects.filter(
                        id_research = research.id,
                        type_research = research.type_id,
                    ))
            return render(request, "meeting/openMeeting.html", {
                'usersInMeeting': usersInMeeting,
                'researchInMeeting': researchInMeeting,
                'usersAcceptedList': usersAcceptedList,
                'usersDeniedList': usersDeniedList,
                'meetingCheckStatus': meetingCheckStatus,
                'acceptToAdminSetting': acceptToAdminSetting,
                'meeting_id': id,
                'RequestNumberList': RequestNumberList,
                'conflictList': conflictList,
                'anotherDocListMki': anotherDocListMki,
            })

    return render(request, "index.html")


@login_required(login_url='/')
def expertResearch(request):
    '''
    The function allows you to answer users who want to be expert in researchs 
    '''
    if check_access(11,2,3, user_roleId=request.user.role_id):
        expertRequests = ExpertRequest.objects.all()
        if request.POST:
            userForLogger = UserModel.User.objects.filter(username=request.POST.get('username')).first()
            #idForLogger = ExpertRequest.objects.filter(id=request.POST.get('id_request')).first()
            if request.POST.get('accept'):
                id_user = UserModel.User.objects.filter(username=request.POST.get('username')).first().id
                ResearchModel.MkiFirstRequestResearch.objects.filter(id=request.POST.get('accept')).update(expert=id_user)
                ExpertRequest.objects.filter(id=request.POST.get('id_request')).delete()
               # logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Одобрил заявку становление ' + str(userForLogger) + ' экспертом в исследовании(ID=' + str(idForLogger) + ')')
            if request.POST.get('decline'):
                ExpertRequest.objects.filter(id=request.POST.get('id_request')).delete()
                #logger_func.setInfoInLogger(user=request.user, datetime=now.strftime("%d-%m-%Y %H:%M"), action='Отклонил заявку становление ' + str(userForLogger) + ' экспертом в исследовании(ID=' + str(idForLogger) + ')')
        return render(request, "meeting/requestExperts.html", {'expertRequests': expertRequests})
    else: return render(request, "index.html")


def editMeeting(request, id):
    '''
    The function allows you to edit researches that were entering in the meeting 
    id = id meeting when we open.
    record = contain QuerySet with research then has meeting_id == id
    '''
    if check_access(11,2,3, user_roleId=request.user.role_id):
        meetingEndCheck = Meetings.objects.filter(id=id).first()
        record = getResearchInMeeting(id)
        if meetingEndCheck.status != 'Created':
            return render(request, "index.html")
        meeting = Meetings.objects.filter(id=id).first()
        researchListMki = ResearchModel.MkiFirstRequestResearch.objects.filter(secretar_accepted=True)
        researchListMed = ResearchModel.MedProductRequestResearch.objects.filter(secretar_accepted=True)
        researchInMeetingList = []
        for research in record:
            researchInMeetingList.append(research)
        if request.POST:
            if request.POST.get('DELETE'):
                type, id = request.POST.get('DELETE').split('.')
                ResearchList.objects.filter(meeting=meeting, research_id=id, research_type=type).delete()
            if request.POST.get('ADD'):
                type, id = request.POST.get('ADD').split('.')
                if ResearchList.objects.filter(meeting=meeting, research_id=id, research_type=type):
                    ResearchList.objects.filter(meeting=meeting, research_id=id, research_type=type).delete()
                ResearchList.objects.create(meeting=meeting, research_id=id, research_type=type)
                return render(request, 'meeting/editMeeting.html', {'record': record, 
                                                            'researchListMki': researchListMki, 
                                                            'researchListMed': researchListMed,
                                                            'researchInMeetingList': researchInMeetingList })


        return render(request, 'meeting/editMeeting.html', {'record': record, 
                                                            'researchListMki': researchListMki, 
                                                            'researchListMed': researchListMed,
                                                            'researchInMeetingList': researchInMeetingList })
    else: return render(request, "index.html")