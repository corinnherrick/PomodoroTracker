import datetime
from django.test import TestCase
from tasks.models import Task, Project
from tasks.serializers import TaskSerializer, ProjectSerializer

class BasicTaskModelTestCase(TestCase):
    def test_can_create_project(self):
        test_project = Project.objects.create(title="Test Project")
        self.assertEqual(test_project.title, "Test Project")
    
    def test_can_create_task(self):
        test_task = Task.objects.create(body="test task")
        self.assertEqual(test_task.body, "test task")
        self.assertEqual(test_task.importance, Task.MEDIUM)
        self.assertTrue(test_task.need_to_happen)
        self.assertEqual(test_task.expected_pomodoros, 1)
        self.assertEqual(test_task.actual_pomodoros, 0)
        self.assertFalse(test_task.completed, False)
        

class BasicTaskSerializerTestCase(TestCase):
    def setUp(self):
        self.test_project = Project.objects.create(title="Test Project")
        self.test_task = Task.objects.create(body="Test Task", due_date=datetime.date(2015, 1, 3))

    def test_can_serialize_project(self):
        serializer = ProjectSerializer(self.test_project)
        self.assertEqual(serializer.data, {'title': 'Test Project'})
        
    def test_can_serialize_task(self):
        serializer = TaskSerializer(self.test_task)
        self.assertEqual(serializer.data, {'body': 'Test Task', 'project': None,
                                           'day': None, 'due_date': datetime.date(2015, 1, 3), 
                                           'importance': Task.MEDIUM, 'need_to_happen': True, 
                                           'expected_pomodoros': 1, 'actual_pomodoros': 0, 
                                           'completed': False  })
