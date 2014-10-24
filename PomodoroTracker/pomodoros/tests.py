import datetime
from django.test import TestCase
from django.test.client import RequestFactory

from pomodoros.models import Pomodoro, Day, Distraction
from pomodoros.serializers import PomodoroSerializer, DaySerializer, DistractionSerializer
from tasks.models import Task

class BasicPomdoroModelTestCase(TestCase):
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


class BasicPomodoroSerializerTestCase(TestCase):
    def setUp(self):
        self.test_day = Day.objects.create(date=datetime.date(2036, 5, 12))
        self.test_pomodoro = Pomodoro.objects.create(day=self.test_day)
        self.test_distraction = Distraction.objects.create(body="Test Distraction",
                                                   pomodoro=self.test_pomodoro,
                                                   status=Distraction.NOT_HANDLED)

    def test_can_serialize_pomodoro(self):
        serializer = PomodoroSerializer(self.test_pomodoro,
                                        context={'request': RequestFactory().get('/')})
        self.assertEqual(serializer.data, {'tasks': [], 
                                           'day': 'http://testserver/days/%d/' % self.test_day.id, 
                                           'completed': False})

    def test_can_serialize_day(self):
        serializer = DaySerializer(self.test_day)
        self.assertEqual(serializer.data, {'date': datetime.date(2036, 5, 12)})
    
    def test_can_serialize_distraction(self):
        serializer = DistractionSerializer(self.test_distraction, 
                                           context={'request': RequestFactory().get('/')})
        self.assertEqual(serializer.data, {'body': "Test Distraction", 
                                           'pomodoro': 'http://testserver/pomodoros/%d/' 
                                                        % self.test_pomodoro.id,
                                           'status': Distraction.NOT_HANDLED})

