from freeadmin import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.app_index),
    url(r'^(\w+)/(\w+)/$', views.table_data_list),
    url(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_change),
    url(r'^(\w+)/(\w+)/add/$', views.table_add),

]
