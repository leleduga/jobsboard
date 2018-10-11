from django.conf.urls import url
from . import views        
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^dashboard$', views.dashboard),
    url(r'^create_job$', views.create_job),
    url(r'^add$', views.add),
    url(r'^viewjob/(?P<id>\d+)', views.viewjob),
    url(r'^logout$', views.logout),
    url(r'^edit$', views.edit),
    url(r'^delete/(?P<id>\d+)', views.delete),
    url(r'^validate_login$', views.validate_login),
 ]                
