from django.db import models

class Task(models.Model):
    """ Represents a single task that the user needs to accomplish.

        Fields:
            * body (required) -- a short (500 char or less) description of the task.
            * project (optional) -- the project model that the task is associated with.
                         If blank, then project is in inbox.
            * day (optional) -- the day model that the task is assigned to be done during.
            * due_date (optional) -- day when the task is due
            * importance[LOW, MEDIUM, HIGH] (default=MEDIUM) -- the importance of a task 
                                                                (distinct from its  urgency)
            * need_to_happen (default=True) -- whether the task needs to be done or is optional
            * expected_pomodoros (default=1) -- how many pomodoros the task is expected to take
            * actual_pomodoros (default=0) -- how many pomodoros the task has taken
            * completed (default=False) -- whether the task has been completed

       Related Models:
            * Pomodoro -- a many to many relationship
    """
    body = models.CharField(max_length=500)
    project = models.ForeignKey('Project', blank=True, null=True)
    day = models.ForeignKey('pomodoros.Day', blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    LOW= 1
    MEDIUM = 2
    HIGH = 3
    IMPORTANCE_CHOICES = (
        (LOW, 'Not Important'),
        (MEDIUM, 'Somewhat Important'),
        (HIGH, 'Very Important'),
    )
    importance = models.PositiveSmallIntegerField(choices=IMPORTANCE_CHOICES, default=2)
    need_to_happen = models.BooleanField(default=True)
    expected_pomodoros = models.PositiveSmallIntegerField(default=1)
    actual_pomodoros = models.PositiveSmallIntegerField(default=0)
    completed = models.BooleanField(default=False)


class Project(models.Model):
    """ Represents a project, an organizational structure for tasks.

        Fields:
            * title (required) -- a short (100 char or less) title for the project
    """
    title = models.CharField(max_length = 100)
