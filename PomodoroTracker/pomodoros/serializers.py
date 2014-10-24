from pomodoros.models import Pomodoro, Day, Distraction
from rest_framework import serializers

class PomodoroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pomodoro
        fields = ('tasks', 'day', 'completed')

class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ('date',)

class DistractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distraction
        fields = ('body', 'pomodoro', 'status')
