#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def get_model_verbose_name(model_obj):

    model_name = model_obj._meta.verbose_name if model_obj._meta.verbose_name else model_obj._meta.verbose_name_plural
    if not model_name:
        model_name = model_obj._meta.model_name
    return model_name


@register.simple_tag
def get_model_name(model_obj):
    return model_obj._meta.model_name


@register.simple_tag
def get_app_name(model_obj):
    return model_obj._meta.app_label


@register.simple_tag
def build_table_row(admin_obj, obj):
    row_ele = ""
    if admin_obj.list_display:
        for column in admin_obj.list_display:
            column_obj = obj._meta.get_field(column)
            if column_obj.choices:
                get_column_data = getattr(obj, "get_%s_display" % column)
                column_data = get_column_data()
            else:
                column_data = getattr(obj, column)
            td_ele = '''<td>%s</td>''' % column_data
            row_ele += td_ele
    else:
        row_ele += "<td>%s</td>" % obj
    return mark_safe(row_ele)


@register.simple_tag
def get_filter_field(filter_column, admin_obj):
    print("admin obj", admin_obj.model, filter_column)

    field_obj = admin_obj.model._meta.get_field(filter_column)
    select_ele = """<select name="%s">""" % filter_column
    for choice in field_obj.get_choices():
        selected_condition = admin_obj.filter_conditions.get(filter_column)
        if selected_condition:  #if none 没有过滤这个条件
            if selected_condition == choice[0]:
                selected = "selected"
            else:
                selected = ""
        else:
            selected = ""
        option_ele = """<option value=%s %s>%s</option>""" % (choice[0], selected, choice[1])
        select_ele += option_ele

    select_ele += "</select>"

    return  mark_safe(select_ele)