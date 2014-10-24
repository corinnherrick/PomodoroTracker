from django.db import models

class Pomodoro(models.Model):
    """ Represents a 25 minute unit of work.

        Fields:
            * tasks (optional) -- the tasks associated with this pomodoro. Many pomodoros
                                  may be associated with the same task and many tasks may
                                  be associated with the same pomodoro.
            * day (required) -- the day when this pomodoro will be completed.
            * completed (default=False) -- whether the pomodoro has been completed
    """
    tasks = models.ManyToManyField('tasks.Task', blank=True)
    day = models.ForeignKey('Day')
    completed = models.BooleanField(default=False)

class Day(models.Model):
    """ Represents a day of work for the user.
    
        Fields:
            * date (required) -- the date of the day.
    """
    date = models.DateField()

class Distraction(models.Model):
    """ Represents a distraction a user encounters during a pomodoro.

        Fields:
            * body (required) -- a short (500 char or less) description of the distraction
            * pomodoro (required) -- the pomodoro the distraction occurred during
            * status[NOT_HANDLED, TASK, IGNORE] (default=NOT_HANDLED) -- what the status
                                                of dealing with the distraction is.
    """
    body = models.CharField(max_length=500)
    pomodoro = models.ForeignKey('Pomodoro')

    NOT_HANDLED = 0
    TASK = 1
    IGNORE = 2
    STATUS_OPTIONS = (
        (NOT_HANDLED, 'To be dealt with.')
        (TASK, 'Became a task.'),
        (INGORE, 'Ignored.'),
    )
    status = models.SmallPositiveIntegerField(choices=STATUS_OPTIONS, default=NOT_HANDLED)
