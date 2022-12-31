from .models import User, Test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm, AddPatientForm, AddDoctorForm, AddTestForm
from django.views.generic import ListView


class SignupView(CreateView):
    model = User
    form_class = SignupForm

    template_name = 'signup.html'


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "GET":
            return render(request,'login.html')
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                print('user or pass is wrong')
    return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

@method_decorator(login_required(login_url='login'),name='dispatch')
class AccountSettingsView(UpdateView):
    model = User
    fields = ['username','email','first_name','last_name']
    template_name = 'account_settings.html'
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user


class add_patientView(CreateView):
    model = User
    form_class = AddPatientForm
    template_name = 'addpatient.html'
    success_url = '/profile/'


class add_doctorView(CreateView):
    model = User
    form_class = AddDoctorForm
    template_name = 'add-doctor.html'
    success_url = '/profile/'

class add_testView(CreateView):
    model = Test
    form_class = AddTestForm
    template_name = 'add-test.html'
    success_url = '/profile/'


class PatientView(ListView):
    model = User
    template_name = 'patients.html'



class DoctorView(ListView):
    model = User
    template_name = 'doctors.html'




class TestView(ListView):
    model = Test
    template_name = 'tests.html'


