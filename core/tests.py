from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from . import views

class EmailResultTests(TestCase):
    def test_email_view_status_code(self):
        url = reverse('email-result')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_sendemail_view_status_code(self):
        url = reverse('email')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    #failed : profile is authenticted. (login required)
    def test_profile_view_status_code(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_guide_view_status_code(self):
        url = reverse('guide')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_contactus_view_status_code(self):
        url = reverse('contact-us')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
# Create your tests here.
