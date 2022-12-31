from django.contrib.auth.forms import UserCreationForm
from .models import User, Test
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']


class AddPatientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','patientstatus']



class AddDoctorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'role']



class AddTestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['usertest','name','test_date','theresult']

