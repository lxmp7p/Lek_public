from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from .views import createMkiResearch
from .views import watchResearchList
from .views import watchResearch
from .views import index
from .views import getMyResearchsStatus
from .views import acceptedResearchsList
from .views import editResearch
from .views import createMkiResearch, createMedResearch, editTeamList

urlpatterns = [
    path('', createMkiResearch,  name='createFirstMki'),
    path('main/', index, name='index'),
    path('watchResearchList/', watchResearchList, name='watchResearchList'),
    path('watchResearch/<int:type>/<int:id>/', watchResearch, name='watchResearch'),
    path('myResearchsStatus', getMyResearchsStatus, name='myResearchsStatus'),
    path('acceptedResearchsList', acceptedResearchsList, name='acceptedResearchsList'),
	 path('createMedResearch/', createMedResearch, name='createMedResearch'),
	 path("editResearch/<int:type>/<int:id>/", editResearch, name='editResearch'),
    path('editTeamList/<int:type>/<int:id>/', editTeamList, name='editTeamList'),
]
