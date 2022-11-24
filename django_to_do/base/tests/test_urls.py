from django.contrib.auth.views import LogoutView
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from base.views import (CustomLoginView, RegisterPage, TaskCreate, TaskDelete,
                        TaskDetail, TaskList, TaskUpdate)


class TestUrls(SimpleTestCase):
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)
        
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)
        
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterPage)

    def test_task_list_url_is_resolved(self):
        url = reverse('tasks')
        self.assertEqual(resolve(url).func.view_class, TaskList)
        
    '''def test_detail_url_is_resolved(self):
        url = reverse('task', args=['some-int'][1])
        self.assertEqual(resolve(url).func.view_class, TaskDetail)'''  #need to add tests for other with int as args
        
    def test_create_url_is_resolved(self):
        url = reverse('task-create')
        self.assertEqual(resolve(url).func.view_class, TaskCreate)
        
        