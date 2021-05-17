from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User as UserModel
from .models import Role
from .forms import UserAccept
import hashlib
from hashlib import sha256
from .forms import ProfileForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from func import check_access
from func import logger_func, search
from logger import models as loggerModels
import datetime
from .models import DocsList
from .models import DocsTypeList, PositionUserList, PositionList
from .functions import set_position, secretarCheck, getUserDocsRequestList
from django.db.models import Q

check_access = check_access.check_access
now = datetime.datetime.now()


def registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            form = user_form.save(commit=False)
            form.sex = request.POST.get('sex')
            form.registration_accepted = False
            form.set_password(form.password)
            form.save()
            return redirect("../")
    else:
        user_form = UserForm()

    return render(request, "registration/register.html", {
        'user_form': user_form,
    })

def auth(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
        if user is not None:
            if user.registration_accepted == 'True':
                login(request, user)
                return render(request, "index.html", )
            else:
                return render(request, "registration/login.html", {'error': 'Вашу заявку еще не приняли!'})
        else:
            return render(request, "registration/login.html", {'error': 'Неверный логин или пароль!'})
    return render(request, "registration/login.html", )

@login_required(login_url='/')
def register_requests(request):
    if check_access(11,2,3, user_roleId=request.user.role_id):
        if request.method == 'POST':
            if 'decline' in request.POST:
                UserModel.objects.filter(username=request.POST.get('username')).delete()
                logger_func.setInfoInLogger(user=request.user,
                                            datetime=now.strftime("%d-%m-%Y %H:%M"),
                                            action='Отклонил заявку ' + str(request.POST.get('username')) + ' на регистрацию')
            if 'accept' in request.POST:
                UserModel.objects.filter(username=request.POST.get('username')).update(registration_accepted=True)
                UserModel.objects.filter(username=request.POST.get('username')).update(role_id=request.POST.get('selected_role'))
                logger_func.setInfoInLogger(user=request.user,
                                            datetime=now.strftime("%d-%m-%Y %H:%M"),
                                            action='Принял заявку ' + str(request.POST.get('username')) + ' на регистрацию назначив роль - ' + str(request.POST.get('selected_role')))
        users = UserModel.objects.filter(registration_accepted=False)
        userList = []
        for user in users:
            userList.append(user)
        return render(request, "registration/registerRequests.html", {"userList": userList, 'form': UserAccept,'roleList': Role.objects.all()})
    else: return render(request, "index.html")

@login_required(login_url='/')
def profile(request, username):
    folder_name = '\photo'
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.base_location = fs.base_location + folder_name
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        UserModel.objects.filter(username=username).update(photo=folder_name[1:] + '\\' + filename)
    form = ProfileForm()
    user = UserModel.objects.filter(username=username)[0]
    return render(request, 'profile/profile.html', {'user': user, 'form':form, 'username': username } )


def passwordChange(request):
    if request.method == 'POST':
        user = authenticate(username=request.user.username, password=request.POST.get('old_password'))
        if user is not None:
            if request.POST.get('new_password') == request.POST.get('repeat_new_password'):
                user.set_password(request.POST.get('new_password'))
                user.save()
                logger_func.setInfoInLogger(user=request.user,
                                            datetime=now.strftime("%d-%m-%Y %H:%M"), 
                                            action='Сменил пароль')
                return redirect("../../../../")
    return render(request, 'profile/password_change_form.html')

@login_required(login_url='/')
def profileDocs(request, username):
    if (check_access(UserModel.objects.filter(role_id=3),
                    UserModel.objects.filter(username=username),
                    user = request.user) == False):
        return render(request, "index.html")
    user = UserModel.objects.filter(username=username).first()
    docsListModel = DocsList.objects.filter(user=user)
    DocsTypeListModel = DocsTypeList.objects.all()
    if request.method == 'POST' and request.FILES:
        file = request.FILES
        key = ''
        for i in file.keys():
            key = i
            fileSave = (file[i])
            fs = FileSystemStorage()
            print(fileSave.name)
            filename = fs.save('docs/' + user.username + '/' + fileSave.name, fileSave)
            if (DocsList.objects.filter(docName = DocsTypeList.objects.filter(id=key).first(), user = user)):
                DocsList.objects.filter(docName = DocsTypeList.objects.filter(id=key).first(), user = user).update(
                                    docName = DocsTypeList.objects.filter(id=key).first(),
                                    file = filename,
                                    user = user)
                UserModel.objects.filter(username=user.username).update(docStatus=False)
            else:
                DocsList.objects.create(docName = DocsTypeList.objects.filter(id=key).first(),
                                        file = filename,
                                        user = user) # <----------- СДЕЛАТЬ ЗАПИСЬ В БД
                UserModel.objects.filter(username=user.username).update(docStatus=False)
    fileListHave = []
    for i in docsListModel:
        fileListHave.append(i)

    return render(request, "profile/profileDocs.html", {'docsListModel': docsListModel,
                                                        'DocsTypeListModel': DocsTypeListModel,
                                                        'fileListHave': fileListHave,
                                                        'username': username,
        })

    
@login_required(login_url='/')
def docsRequestList(request):
    if check_access(11,2,3, user_roleId=request.user.role_id):
        records = getUserDocsRequestList()
        return render(request, "profile/DocsRequestList.html", {'record': records})
    return render(request, "index.html")

@login_required(login_url='/')
def docsRequest(request, user_id):
    if check_access(11,2,3, user_roleId=request.user.role_id):
        if request.method == 'POST':
            if request.POST.get('ACCEPT'):
                UserModel.objects.filter(id=user_id).update(docStatus=True)
            elif request.POST.get('DENIED'):
                UserModel.objects.filter(id=user_id).update(docStatus=False)
            records = getUserDocsRequestList()
            return render(request, "profile/DocsRequestList.html", {'record': records})
        records = DocsList.objects.filter(user_id=user_id)
        return render(request, 'profile/watchDoc.html', {'records':records})
    return render(request, "index.html")

@login_required(login_url='/')
def userSetting(request, username): 
    if check_access(11,2,3, user_roleId=request.user.role_id):
        user = UserModel.objects.filter(username=username).first()
        options = PositionUserList.objects.filter(user=user)
        if request.POST:
            typeVoiceList = []
            for i in request.POST:  
                typeVoiceList.append(i)
            typeVoiceList = typeVoiceList[1:]
            for record in PositionList.objects.all():
                position = record
                set_position(position, user, request.POST.get(typeVoiceList[0]))
                del typeVoiceList[0]

        return render(request, 'profile/userSetting.html', {'options': options, 
                                                            'username': username,
                                                            })
    return render(request, "index.html")