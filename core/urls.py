
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
path('',login_page,name='login'),
path('signup/',SignupView.as_view(),name='signup'),
path('logout/',logout_user,name='logout'),

path('add-patient/',add_patientView.as_view(),name='add-patient'),
path('patients/', PatientView.as_view(),name='patients'),

path('add-doctor/',add_doctorView.as_view(),name='add-doctor'),
path('doctors/', DoctorView.as_view(),name='doctors'),

path('add-test/',add_testView.as_view(),name='add-test'),
path('tests/', TestView.as_view(),name='tests'),

path('profile/',profile,name='profile'), #name for href in <a>
path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),

]
