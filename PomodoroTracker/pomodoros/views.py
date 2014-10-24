from django.shortcuts import render
from rest_framework import viewsets
from pomodoros.serializers import PomodoroSerializer, DaySerializer, DistractionSerializer
from pomodoros.models import Pomodoro, Day, Distraction


class PomodoroViewSet(viewsets.ModelViewSet):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class DistractionViewSet(viewsets.ModelViewSet):
    queryset = Distraction.objects.all()
    serializer_class = DistractionSerializer
