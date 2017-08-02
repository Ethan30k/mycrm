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
    field_obj = admin_obj.model._meta.get_field(filter_column)
    select_ele = """<select name="%s">""" % filter_column
    for choice in field_obj.get_choices():
        selected_condition = admin_obj.filter_conditions.get(filter_column)
        # print(field_obj.get_choices())
        if selected_condition is not None:  # if none 没有过滤这个条件
            if selected_condition == str(choice[0]):

                selected = "selected"
            else:
                selected = ""
        else:
            selected = ""
        option_ele = """<option value="%s" %s>%s</option>""" % (choice[0], selected, choice[1])
        select_ele += option_ele

    select_ele += "</select>"

    return mark_safe(select_ele)


@register.simple_tag
def generate_filter_url(admin_obj):
    url = ""
    for k, v in admin_obj.filter_conditions.items():
        url += "&%s=%s" % (k, v)
    return url


@register.simple_tag
def get_orderby_key(request, column):
    current_order_by_key = request.GET.get("_o")
    # print(column, current_order_by_key)
    if current_order_by_key is not None:    # 肯定有某列被排序
        if current_order_by_key == column:  # 当前这列被排序
            return "-%s" % column
        else:
            return column.strip("-")
    return column


@register.simple_tag
def display_order_by_icon(request, column):
    current_order_by_key = request.GET.get("_o")
    # print(column, current_order_by_key)
    if current_order_by_key is not None:
        if current_order_by_key.strip("-") == column:
            if current_order_by_key.startswith("-"):
                ele = """<span class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>"""
                return mark_safe(ele)
            else:
                ele = """<span class="glyphicon glyphicon-menu-up" aria-hidden="true"></span>"""
                return mark_safe(ele)
        else:
            return ""
    else:
        return ""


@register.simple_tag
def get_current_orderby_key(request):
    # 获取当前正在排序的字段名
    current_order_by_key = request.GET.get("_o")
    return current_order_by_key


@register.simple_tag
def generater_order_by_url(request):
    current_order_by_key = request.GET.get("_o")
    if current_order_by_key is not None:
        return "&_o=%s" % current_order_by_key
    return ""
