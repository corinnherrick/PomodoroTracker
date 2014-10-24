from django.shortcuts import render
from rest_framework import viewsets
from tasks.serializers import TaskSerializer, ProjectSerializer
from tasks.models import Task, Project

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
