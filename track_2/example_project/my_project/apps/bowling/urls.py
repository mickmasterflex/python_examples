from django.conf.urls import *

from bowling import views

urlpatterns = patterns('bowling.views',
    url(r'^score/$', views.ScoreListView.as_view(),
        name='score'),
)

