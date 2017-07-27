from django.conf.urls import url, include
from django.contrib import admin

from crm import views

urlpatterns = [
    url(r'^$', views.dashboard, name="sales_dashboard"),
    url(r'^customers/$', views.customers, name="customers"),
]
