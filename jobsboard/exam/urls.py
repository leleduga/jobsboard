
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('apps.examapp.urls')),
    # url(r'^examapp', include('apps.examapp.urls')),
    # url(r'^add', include('apps.examapp.urls')),
    # url(r'^dashboard', include('apps.examapp.urls')),
    # url(r'^edit', include('apps.examapp.urls')),
    # url(r'^viewjob', include('apps.examapp.urls')),
]
