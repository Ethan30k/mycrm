from django.shortcuts import render, redirect
from django import conf
from freeadmin import app_config
import json
from freeadmin import forms
from django.db.models import Q
from freeadmin import base_admin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required
def app_index(request):
    return render(request, 'freeadmin/app_index.html', {"site": base_admin.site})


def filter_querysets(request, queryset):
    conditions = {}
    for k, v in request.GET.items():
        if k in ("page", "_o", "_q"):
            continue
        if v:
            conditions[k] = v

    query_res = queryset.filter(**conditions)
    return query_res, conditions


def get_orderby(request, queryset):
    order_by_key = request.GET.get("_o")
    if order_by_key == "None":
        order_by_key = None
    if order_by_key is not None:  # has sort condition
        query_res = queryset.order_by(order_by_key)
    else:
        query_res = queryset.order_by("-id")
    return query_res


def get_queryset_search_result(request, queryset, admin_obj):
    search_key = request.GET.get("_q", "")
    q_obj = Q()
    q_obj.connector = "OR"
    for column in admin_obj.search_fields:
        q_obj.children.append(("%s__contains" % column, search_key))

    res = queryset.filter(q_obj)
    return res


def table_data_list(request, app_name, model_name):
    admin_obj = base_admin.site.registered_sites[app_name][model_name]

    if request.method == "POST":
        action = request.POST.get("action_select")
        selected_ids = request.POST.get("selected_ids")
        selected_ids = json.loads(selected_ids)
        print("action:", selected_ids, action)
        selected_objs = admin_obj.model.objects.filter(id__in=selected_ids)
        action_func = getattr(admin_obj, action)
        action_func(request, selected_objs)

    obj_list = admin_obj.model.objects.all()
    queryset, conditions = filter_querysets(request, obj_list)
    # after search
    queryset = get_queryset_search_result(request, queryset, admin_obj)

    sorted_queryset = get_orderby(request, queryset)

    paginator = Paginator(sorted_queryset, admin_obj.list_per_page)  # Show 25 contacts per page

    if request.GET.get('page') is not None:
        page = int(request.GET.get('page'))
    else:
        page = 1
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objs = paginator.page(paginator.num_pages)

    admin_obj.querysets = objs

    admin_obj.filter_conditions = conditions
    return render(request, "freeadmin/table_data_list.html", locals())


def table_change(request, app_name, model_name, obj_id):
    admin_obj = base_admin.site.registered_sites[app_name][model_name]

    model_form = forms.CreateModelForm(request, admin_obj=admin_obj)
    obj = admin_obj.model.objects.get(id=obj_id)
    if request.method == "GET":
        obj_form = model_form(instance=obj)
    elif request.method == "POST":
        obj_form = model_form(instance=obj, data=request.POST)
        if obj_form.is_valid():
            obj_form.save()
        # print(obj_form)
    return render(request, "freeadmin/table_change.html", locals())


def table_add(request, app_name, model_name):
    admin_obj = base_admin.site.registered_sites[app_name][model_name]
    model_form = forms.CreateModelForm(request, admin_obj=admin_obj)
    if request.method == "GET":
        obj_form = model_form()
    elif request.method == "POST":
        obj_form = model_form(data=request.POST)
        if obj_form.is_valid():
            obj_form.save()
        if not obj_form.errors:
            return redirect("/freeadmin/%s/%s" % (app_name, model_name))
    return render(request, "freeadmin/table_add.html", locals())