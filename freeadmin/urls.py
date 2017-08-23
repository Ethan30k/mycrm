from freeadmin import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.app_index, name='app_index'),
    url(r'^(\w+)/(\w+)/$', views.table_data_list, name='table_list'),
    url(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_change, name="table_change"),
    url(r'^(\w+)/(\w+)/add/$', views.table_add, name="table_add"),

]
