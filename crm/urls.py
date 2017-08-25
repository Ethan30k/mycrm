from django.conf.urls import url, include
from django.contrib import admin

from crm import views

urlpatterns = [
    url(r'^$', views.dashboard, name="sales_dashboard"),
    url(r'^customers/$', views.customers, name="customers"),
    url(r'customer/enrollment/(\d+)/$', views.customer_enrollment, name="customer_enrollment"),
    url(r'student/enrollment/(\d+)/$', views.stu_enrollment, name="stu_enrollment"),
    url(r'customer_enrollment/audit/(\d+)/$', views.enrollment_audit, name="enrollment_audit"),
]
