from tasks.models import Task, Project
from rest_framework import serializers

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('body', 'project', 'day', 'due_date', 'importance', 'need_to_happen',
                  'expected_pomodoros', 'actual_pomodoros', 'completed',)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('title',)
        
