from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import BooleanField, ChoiceField, Select


# Create your models here.

class User(AbstractUser):
    status = BooleanField()


    ADMIN = 1
    DOCTOR = 2
    PATIENT = 3

    STATUS_CHOICES = (
        (True, 'Infected'),
        (False, 'Not infected')
    )
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),

    )
    role = models.PositiveSmallIntegerField(default= PATIENT,choices=ROLE_CHOICES, blank=True, null=True)
    patientstatus = models.BooleanField(default= False,choices=STATUS_CHOICES, blank=True, null=True)



class Test(models.Model):
    usertest = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    test_date = models.DateField()

    RESULT_CHOICES = (
        (True, 'Infected'),
        (False, 'Not infected')
    )
    theresult = models.BooleanField(default= False,choices=RESULT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name