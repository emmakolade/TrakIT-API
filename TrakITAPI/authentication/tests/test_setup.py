from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):
    self.register_url=reverse('register')