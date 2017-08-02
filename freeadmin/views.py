from django.shortcuts import render
from django import conf
# Create your views here.
from freeadmin import app_config
from freeadmin import base_admin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def app_index(request):
    # for app in conf.settings.INSTALLED_APPS:
    #     print(app)
    print("registered_sites", base_admin.site.registered_sites)
    return render(request, 'freeadmin/app_index.html', {"site": base_admin.site})


def filter_querysets(request, queryset):
    conditions = {}
    for k, v in request.GET.items():
        if k in ("page", "_o"):
            continue
        if v:
            conditions[k] = v
    print("conditions:", conditions)

    query_res = queryset.filter(**conditions)
    return query_res, conditions


def get_orderby(request, queryset):
    order_by_key = request.GET.get("_o")
    if order_by_key == "None":
        order_by_key = None
    if order_by_key is not None:
        print("1", order_by_key, type(order_by_key))
        query_res = queryset.order_by(order_by_key)
    else:
        query_res = queryset
        print("2", order_by_key, type(order_by_key))
    return query_res


def table_data_list(request, app_name, model_name):
    admin_obj = base_admin.site.registered_sites[app_name][model_name]
    obj_list = admin_obj.model.objects.all()
    queryset, conditions = filter_querysets(request, obj_list)
    print("---->", queryset)

    sorted_queryset = get_orderby(request, queryset)

    paginator = Paginator(sorted_queryset, admin_obj.list_per_page)  # Show 25 contacts per page

    if request.GET.get('page') is not None:
        page = int(request.GET.get('page'))
    else:
        page = 1
    print(page)
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

