from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
import tasks.views
import pomodoros.views

router = routers.DefaultRouter()
router.register(r'tasks', tasks.views.TaskViewSet)
router.register(r'projects', tasks.views.ProjectViewSet)
router.register(r'pomodoros', pomodoros.views.PomodoroViewSet)
router.register(r'days', pomodoros.views.DayViewSet)
router.register(r'distractions', pomodoros.views.DistractionViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PomodoroTracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
