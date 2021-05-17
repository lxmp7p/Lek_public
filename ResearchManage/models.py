from django.db import models
from django import forms
from UserControl.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from UserControl.models import User
from UserControl.models import PI_BirthDay



class logAboutResearch(models.Model):
    condition = models.CharField(max_length=100, blank=True, null=True)
    id_research = models.CharField(max_length=100, blank=True, null=True)
    type_research = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = "logAboutResearch" 

class ConflictsInterests(models.Model):
    fio = models.CharField(max_length=100)
    id_research = models.CharField(max_length=100)
    type_research = models.CharField(max_length=100)
    class Meta:
        db_table = "ConflictsInterests" 

class RequestsResearchsList(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = "RequestsResearchsList" 

class RequestNumber(models.Model):
    id_research = models.CharField(max_length=100)
    type_research = models.CharField(max_length=100)
    class Meta:
        db_table = "RequestNumber"     

class NameAnotherDocument(models.Model):
    """docstring for TypeDocument"""
    name = models.CharField(max_length=100)
    def __init__(self, arg):
        super(TypeDocument, self).__init__()
        self.arg = arg
    class Meta:
        db_table = "NameAnotherDocument"        

class AnotherDoc(models.Model):
    """docstring for AnotherDocuments"""
    id_research = models.CharField(max_length=100)
    type_research = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    class Meta:
        abstract = True

class AnotherDocuments(AnotherDoc):
    """docstring for AnotherDocuments"""
    name_document = models.ForeignKey(NameAnotherDocument, on_delete=models.CASCADE, related_name='name_documents')
    class Meta:
        db_table = "AnotherDocuments"    

class AnotherDocumentsHistory(AnotherDoc):
    name_document = models.ForeignKey(NameAnotherDocument, on_delete=models.CASCADE, related_name='name_document_h')
    ver = models.IntegerField()
    class Meta:
        db_table = "AnotherDocumentsHistory"     


class MkiFirstResearch(models.Model):
    subpoena = models.FileField(upload_to='temp/')
    addedInMeeting = models.BooleanField(default=False)
    report = models.FileField(upload_to='temp/')
    acceptedOnMeeting = models.CharField(max_length=20)
    protocol_number = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    secretar_accepted = models.CharField(max_length=10)
    secretar_accepted_date = models.DateField(blank=True, null=True)
    date_created = models.CharField(max_length=50)
    document = models.FileField(upload_to='temp/')
    status = models.CharField(max_length=10)
    list_members = models.FileField(upload_to='temp/')
    ver_bio = models.CharField(max_length=50)
    accept_research = models.FileField(upload_to='temp/', blank=True, null=True)
    accept_research_version = models.CharField(max_length=50, blank=True, null=True)
    accept_research_date = models.DateField(blank=True, null=True)
    protocol_research = models.FileField(upload_to='temp/')
    protocol_research_version = models.CharField(max_length=50)
    protocol_research_date = models.DateField()
    contract = models.FileField(upload_to='contract/')
    contract_date = models.DateField()
    advertising = models.FileField(upload_to='temp/', blank=True, null=True)
    write_objects = models.FileField(upload_to='temp/', blank=True, null=True)
    name_another_doc = models.CharField(max_length=50, blank=True, null=True)
    another_doc = models.FileField(upload_to='another_doc/', blank=True, null=True)
    another_doc_version = models.CharField(max_length=50, blank=True, null=True)
    another_doc_date = models.DateField(blank=True, null=True)
    class Meta:
        abstract = True

class MkiFirstRequestResearch(MkiFirstResearch):
    type = models.ForeignKey(RequestsResearchsList, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    main_researcher = models.ForeignKey(PI_BirthDay, on_delete=models.CASCADE, related_name='FIOS')
    expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_expert', blank=True, null=True)
    class Meta:
        db_table = "MkiFirstRequestResearch"

class MkiFirstRequestResearchHistory(MkiFirstResearch):
    type = models.ForeignKey(RequestsResearchsList, on_delete=models.CASCADE, related_name='type_h')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_h')
    main_researcher = models.ForeignKey(PI_BirthDay, on_delete=models.CASCADE, related_name='FIOS_h')
    expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_expert_h', blank=True, null=True)
    datetime_edit = models.DateTimeField(blank=True, null=True)
    research = models.ForeignKey(MkiFirstRequestResearch, on_delete=models.CASCADE, related_name='research_h')
    ver = models.IntegerField()
    class Meta:
        db_table = "MkiFirstRequestHistory"
        
class MedProductRequestResearch(models.Model):
    addedInMeeting = models.BooleanField(default=False)
    type = models.ForeignKey(RequestsResearchsList, on_delete=models.CASCADE)
    report = models.FileField(upload_to='temp/')
    acceptedOnMeeting = models.CharField(max_length=20)
    formular_request = models.FileField(upload_to='temp/')
    teamList = models.FileField(upload_to='temp/')
    version_science_bio = models.FileField(upload_to='temp/')  #изменить название столбца
    permission_FS = models.FileField(upload_to='temp/')
    conclusion_ethics = models.FileField(upload_to='temp/')
    program_klin_research = models.FileField(upload_to='temp/')
    form_inf_list = models.FileField(upload_to='temp/')
    registration_cards = models.FileField(upload_to='temp/')
    another_materials = models.FileField(upload_to='temp/')
    info_payout = models.FileField(upload_to='temp/')
    brochure_researcher = models.FileField(upload_to='temp/')
    rukovodstvo = models.FileField(upload_to='temp/')
    technical_file = models.FileField(upload_to='temp/')
    polozhenie_o_soglasii = models.FileField(upload_to='temp/')
    dublicat_dogovor = models.FileField(upload_to='temp/')
    last_solutions = models.FileField(upload_to='temp/')
    info_med_company = models.FileField(upload_to='temp/')
    another_doc_expertize = models.FileField(upload_to='temp/')

    secretar_accepted = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_med')
    status = models.CharField(max_length=10, blank=True, null=True)
    expert = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_expert_med', blank=True, null=True)

    class Meta:
        db_table = "MedProductRequestResearch"



