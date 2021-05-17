from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from ResearchManage import models as ResearchModel
from UserControl.models import User


class Meetings(models.Model): 
    date = models.DateField()
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    report = models.FileField(upload_to='temp/')
    subpoena = models.FileField(upload_to='temp/')

class UserList(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserList')
    meeting = models.ForeignKey(Meetings, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

class ResearchList(models.Model):
    research_id = models.CharField(max_length=100)
    research_type = models.CharField(max_length=100)
    meeting = models.ForeignKey(Meetings, on_delete=models.CASCADE)

class VoteList(models.Model):
    research_id = models.CharField(max_length=100)
    type_res = models.CharField(max_length=100)
    username_vote = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_vote')
    meeting_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    message = models.CharField(max_length=100,  blank=True, null=True)

class ExpertRequest(models.Model):
    user_expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expert_request')
    research = models.ForeignKey(ResearchModel.MkiFirstRequestResearch, on_delete=models.CASCADE, related_name='ResearchList_Expert')