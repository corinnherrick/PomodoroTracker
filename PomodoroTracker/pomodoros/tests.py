import datetime
from django.test import TestCase
from pomodoros.models import Pomodoro, Day, Distraction
from tasks.models import Task

class BasicPomdoroModelTestcase(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(body="test task");

    def test_can_create_day(self):
        test_day = Day.objects.create(date=datetime.date(2014, 12, 24))        
        self.assertEqual(test_day.date, datetime.date(2014, 12, 24))

    def test_can_create_pomodoro(self):
        test_day = Day.objects.create(date=datetime.date(2014, 12, 24))
        test_pomodoro = self.test_task.pomodoros.create(day=test_day)
        
        self.assertEqual(test_pomodoro.tasks.all()[0], self.test_task)
        self.assertEqual(test_pomodoro.day, test_day)
        self.assertEqual(test_pomodoro.completed, False)
    
    def test_can_create_distraction(self):        
        test_day = Day.objects.create(date=datetime.date(2014, 12, 24))        
        test_pomodoro = Pomodoro.objects.create(day=test_day)
        test_distraction = Distraction.objects.create(body="test distraction", 
                                                      pomodoro=test_pomodoro)
        self.assertEqual(test_distraction.body, "test distraction")
        self.assertEqual(test_distraction.pomodoro, test_pomodoro)
        self.assertEqual(test_distraction.status, Distraction.NOT_HANDLED)
