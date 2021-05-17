from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from .views import registration
from .views import register_requests
from .views import profile
from .views import auth
from .views import passwordChange
from .views import profileDocs
from .views import userSetting
from .views import docsRequest
from .views import docsRequestList


urlpatterns = [
    path('registerList/', register_requests,  name='register_requests'),
    path('registration/', registration,  name='registration'),
    path('', auth, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>', profile, name='profile'),
    path('password-change/', passwordChange, name='password_change'),
    path('profileDocs/<str:username>', profileDocs, name='profileDocs'),
    path('docsRequestList/', docsRequestList, name='docsRequestList'),
    path('docsRequest/<int:user_id>', docsRequest, name='docsRequest'),
    path('userSetting/<str:username>', userSetting, name='userSetting'),
]
