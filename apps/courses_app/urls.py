from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^confirm_process/(?P<id>\d+)$', views.confirm),
    url(r'^cancel$', views.index),
    url(r'^confirmed/(?P<id>\d+)$', views.confirmed)
]
