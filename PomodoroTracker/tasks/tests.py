from django.test import TestCase
from tasks.models import Task, Project

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
        
