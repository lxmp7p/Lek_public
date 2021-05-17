from .models import User as UserModel
from .models import PositionUserList, PositionList, DocsList

def set_position(position, user, voice):
    if voice == '1':
        if PositionUserList.objects.filter(position=position, user=user, status='True'):
            PositionUserList.objects.filter(position=position, user=user, status='True').delete()
        if PositionUserList.objects.filter(position=position, user=user, status='False'):
            PositionUserList.objects.filter(position=position, user=user, status='False').delete()
        PositionUserList.objects.create(position=position, user=user, status='True')
    elif voice == '0': 
        if PositionUserList.objects.filter(position=position, user=user, status='False'):
            PositionUserList.objects.filter(position=position, user=user, status='False').delete()
        if PositionUserList.objects.filter(position=position, user=user, status='True'):
            PositionUserList.objects.filter(position=position, user=user, status='True').delete()
        PositionUserList.objects.create(position=position, user=user, status='False')

def secretarCheck(user):
    if (user.role_id == 3):
        return True
    else:
        return False

def getUserDocsRequestList():
    record = DocsList.objects.all().values('user')
    bd = []
    idInRecord = []
    for i in record:
        if i['user'] not in idInRecord:
            idInRecord.append(i['user'])
    for userId in idInRecord:
        user = UserModel.objects.filter(id=userId).first()
        if user.docStatus != 'True':
            bd.append({'user_id': userId, 'FIO': str(user.last_name) + ' ' + str(user.first_name) + ' ' + str(user.middle_name)})
    return bd