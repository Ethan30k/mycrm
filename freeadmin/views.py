from django.shortcuts import render
from django import conf
# Create your views here.
from freeadmin import app_config
from freeadmin import base_admin


def app_index(request):
    # for app in conf.settings.INSTALLED_APPS:
    #     print(app)
    print("registered_sites", base_admin.site.registered_sites)
    return render(request, 'freeadmin/app_index.html', {"site": base_admin.site})


def filter_querysets(request, queryset):
    conditions = {}
    for k, v in request.GET.items():
        if v:
            conditions[k] = v
    print("conditions:", conditions)

    query_res = queryset.filter(**conditions)
    return query_res, conditions


def table_data_list(request, app_name, model_name):
    admin_obj = base_admin.site.registered_sites[app_name][model_name]
    obj_list = admin_obj.model.objects.all()
    queryset, conditions = filter_querysets(request, obj_list)
    print("---->", queryset)
    admin_obj.querysets = queryset
    admin_obj.filter_conditions = conditions
    return render(request, "freeadmin/table_data_list.html", locals())

