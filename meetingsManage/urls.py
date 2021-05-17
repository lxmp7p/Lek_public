from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from .views import createMeeting
from .views import watchMeeting
from .views import openMeeting
from .views import expertResearch
from .views import editMeeting, watchMeetingEnded, checkConflict


urlpatterns = [
    path('', createMeeting,  name='createMeeting'),
    path('watchMeeting/', watchMeeting,  name='watchMeeting'),
    path('meeting/<int:id>/', openMeeting,  name='openMeeting'),
    path('expertResearch/', expertResearch,  name='expertResearch'),
    path('editMeeting/<int:id>/', editMeeting, name='editMeeting'),
	path('watchMeetingEnded/', watchMeetingEnded,  name='watchMeetingEnded'),
    path('checkConflict/', checkConflict, name='checkConflict'),
 
]
