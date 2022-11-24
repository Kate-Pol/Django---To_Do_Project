from django.test import TestCase
from base.models import Task

class BasicTest(TestCase):

    def test_fields(self):
        task = Task()
        task.title = "Make a new tests"
        task.description = "Practice new types of tests"
        task.save()
        
        record = Task.objects.get(pk=1)
        self.assertEqual(record, task)
        
        