#!/usr/bin/env python
# -*- coding: utf-8 -*-


from crm import models
from freeadmin.base_admin import site, BaseAdmin

# print("freeadmin crm", models.Customer)


class CustomerAdmin(BaseAdmin):
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'date')
    list_filter = ('source', 'status', 'consultant')
    search_fields = ('qq', 'name')
    list_editable = ('status',)


site.register(models.Customer, CustomerAdmin)
site.register(models.CourseRecord)