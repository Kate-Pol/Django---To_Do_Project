from django.test import TestCase, Client
from django.urls import reverse
from base.models import Task


'''
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        
    def test_login_GET(self):
        client = Client()
        response = client.get(reverse('task'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')
        '''