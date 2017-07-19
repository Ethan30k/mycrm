from django.conf.urls import url, include
from django.contrib import admin

from crm import views

urlpatterns = [
    url(r'^$', views.dashboard),
]
