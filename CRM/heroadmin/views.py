from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django import conf
from django.contrib.auth.decorators import login_required
from heroadmin import app_setup
from heroadmin.sites import site
from django.core.paginator import Paginator
from crm01 import models

app_setup.heroadmin_auto_discover()

# Create your views here.

print("sites", site.enabled_admin)


def acc_login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('UserName')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            print('passed authentication')
            login(request, user)
            return redirect(request.GET.get('next', '/heroadmin/'))
        else:
            error_msg = "Wrong username or password."
            print('username or password error')
    return render(request, 'heroadmin/login.html', {'error_msg': error_msg})


def acc_logout(request):
    logout(request)
    return redirect('/heroadmin/login/')


def app_index(request):
    return render(request, 'heroadmin/app_index.html', {'site': site})


def get_filter_result(request, querysets):
    filter_conditions = {}
    for key, val in request.GET.items():
        if key in ('_page', '_o'): continue
        if val:
            filter_conditions[key] = val
    print("filter_conditions", filter_conditions)
    return querysets.filter(**filter_conditions), filter_conditions


@login_required
def table_obj_list(request, app_name, model_name):
    """取出指定model里的数据返回给前端"""
    print("app_name,model_name", site.enabled_admin[app_name][model_name])
    admin_class = site.enabled_admin[app_name][model_name]
    print("REQUEST.GET:", request.GET)

    querysets = admin_class.model.objects.all()

    querysets, filter_conditions = get_filter_result(request, querysets)
    admin_class.filter_conditions = filter_conditions

    # sorted querysets
    querysets, sorted_column = get_orderby_result(request, querysets, admin_class)

    paginator = Paginator(querysets, 2)  # Show 25 contacts per page

    _page = request.GET.get('_page')
    querysets = paginator.get_page(_page)
    # return render(request, 'list.html', {'contacts': contacts})

    return render(request, 'heroadmin/table_obj_list.html',
                  {'querysets': querysets,
                   'admin_class': admin_class,
                   'app_name': app_name,
                   'sorted_column': sorted_column})


def get_orderby_result(request, querysets, admin_class):
    """排序"""
    current_ordered_column = {}
    orderby_index = request.GET.get('_o')
    if orderby_index:
        orderby_key = admin_class.list_display[abs(int(orderby_index))]
        current_ordered_column[orderby_key] = orderby_index  # 为了让前端知道当前排序的列

        if orderby_index.startswith('-'):
            orderby_key = "-" + orderby_key
        return querysets.order_by(orderby_key), current_ordered_column
    else:
        return querysets


def test(request):
    return render(request, 'heroadmin/test.html')
