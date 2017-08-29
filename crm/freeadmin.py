#!/usr/bin/env python
# -*- coding: utf-8 -*-


from crm import models
from freeadmin.base_admin import site, BaseAdmin


class CustomerAdmin(BaseAdmin):
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'date', 'stu_enrollment')
    list_filter = ('source', 'status', 'consultant')
    search_fields = ('qq', 'name', 'status')
    list_editable = ('status',)
    readonly_fields = ('qq', 'name')
    actions = ['change_status']

    filter_horizontal = ('consult_courses',)

    def change_status(self, request, querysets):
        print("change status", querysets)
        querysets.update(status=0)

    change_status.short_description = "改变报名状态"


class CourseAdmin(BaseAdmin):
    list_display = ('id', 'name', 'outline', 'price')


class ClassListAdmin(BaseAdmin):
    list_display = ('id', 'course', 'semester')


class CourseRecordAdmin(BaseAdmin):
    list_display = ('id', 'class_grade', 'day_number', 'teacher', 'CourseContent')
    # list_filter = ('day_number',)
    search_fields = ('day_number',)
    actions = ['change_status']

    def change_status(self, request, querysets):
        print("change status", querysets)

site.register(models.Customer, CustomerAdmin)
site.register(models.ClassList, ClassListAdmin)
site.register(models.CourseRecord, CourseRecordAdmin)
site.register(models.Course, CourseAdmin)
