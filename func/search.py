from logger import models as LoggerModel
from UserControl import models as UserModel
from ResearchManage import models as ResearchModel

def searchUsernameInLogger(username):
	return LoggerModel.LoggerRecords.objects.filter(username=username)

def searchFIO(wordList):
	records = UserModel.User.objects.filter(last_name='fixToSearch')
	for word in wordList:
		if UserModel.User.objects.filter(first_name=word):
			records = records | UserModel.User.objects.filter(first_name=word)
		if UserModel.User.objects.filter(last_name=word):
			records = records | UserModel.User.objects.filter(last_name=word)
		if UserModel.User.objects.filter(middle_name=word):
			records = records | UserModel.User.objects.filter(middle_name=word)
		if UserModel.User.objects.filter(username=word):
			records = records | UserModel.User.objects.filter(username=word)
	return records

def searchResearchList(protocol_find):
	researchFinded = ResearchModel.MkiFirstRequestResearch.objects.filter(protocol_number=protocol_find)
	return researchFinded