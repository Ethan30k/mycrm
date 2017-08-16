#!/usr/bin/env python
# -*- coding: utf-8 -*-


from crm import models
from freeadmin.base_admin import site, BaseAdmin

# print("freeadmin crm", models.Customer)


class CustomerAdmin(BaseAdmin):
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'date')
    list_filter = ('source', 'status', 'consultant')
    search_fields = ('qq', 'name', 'status')
    list_editable = ('status',)
    readonly_fields = ('qq', 'name')
    actions = ['change_status']

    def change_status(self, request, querysets):
        print("change status", querysets)
        querysets.update(status=1)

    change_status.short_description = "改变报名状态"


class CourseAdmin(BaseAdmin):
    list_display = ('name', 'outline', 'price')


class ClassListAdmin(BaseAdmin):
    list_display = ('course', 'semester')

site.register(models.Customer, CustomerAdmin)
site.register(models.ClassList, ClassListAdmin)
site.register(models.CourseRecord)
site.register(models.Course, CourseAdmin)