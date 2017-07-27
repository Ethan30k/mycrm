from freeadmin import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.app_index),
    url(r'^(\w+)/(\w+)/$', views.table_data_list),

]
