from django.template import Library
from django.utils.safestring import mark_safe
import datetime

register = Library()


@register.simple_tag
def bulid_table_row(obj, admin_class):
    """生成一条记录的html element"""

    ele = ""
    if admin_class.list_display:
        for column_name in admin_class.list_display:
            column_obj = admin_class.model._meta.get_field(column_name)
            if column_obj.choices:  # get_xxx_dispaly
                column_data = getattr(obj, 'get_%s_display' % column_name)()
            else:
                column_data = getattr(obj, column_name)
            td_ele = "<td>%s</td>" % column_data
            ele += td_ele
    else:
        td_ele = "<td>%s</td>" % obj
        ele += td_ele
    return mark_safe(ele)


@register.simple_tag
def build_filter_ele(filter_column, admin_class):
    """"""
    column_obj = admin_class.model._meta.get_field(filter_column)
    try:
        filter_ele = "<select name='%s'>" % filter_column
        for choice in column_obj.get_choices():
            selected = ''
            if filter_column in admin_class.filter_conditions:  # 当前字段被过滤了
                if str(choice[0]) == admin_class.filter_conditions.get(filter_column):  # 当前值被选中了
                    selected = 'selected'
            option = "<option value='%s' %s>%s</option>" % (choice[0], selected, choice[1])
            filter_ele += option
    except Exception as e:
        print("err:", e)
        filter_ele = "<select name='%s_gte'>" % filter_column
        if column_obj.get_internal_type() in ('DateField', 'DateTimeField'):
            time_obj = datetime.datetime.now()
            time_list = (
                ('', '----------'),
                (time_obj, '今天'),
                (time_obj - datetime.timedelta(7), '七天内'),
                (time_obj.replace(day=1), '本月'),
                (time_obj - datetime.timedelta(90), '三个月内'),
                (time_obj.replace(month=1, day=1), '本年'),
                ('', '所有日期'),
            )
            for i in time_list:
                selected = ''
                filter_column = "%s__gte" % filter_column

                time_to_str = '' if not i[0] else str(i[0])[0:10]
                if filter_column in admin_class.filter_conditions:  # 当前字段被过滤了
                    print("filter_column>>>", filter_column)
                    if time_to_str == admin_class.filter_conditions.get(filter_column):  # 当前值被选中了
                        selected = 'selected'
                option = "<option value='%s' %s>%s</option>" % \
                         (time_to_str, selected, i[1])
                filter_ele += option

    filter_ele += "</select>"
    return mark_safe(filter_ele)


@register.simple_tag
def get_model_name(admin_class):
    return admin_class.model._meta.model_name.upper()


@register.simple_tag
def render_paginator(querysets):
    layui_disabled = ""
    if querysets.number - 1 == 0:
        layui_disabled = "layui-disabled"
    ele = """
    <div id="demo4">
        <div class="layui-box layui-laypage layui-laypage-default" id="layui-laypage-7">
            <a href='?_page=%s' class='layui-laypage-prev %s' data-page='%s'>上一页</a>
    """ % (querysets.number - 1 if querysets.number - 1 != 0 else '', layui_disabled, querysets.number - 1)
    for i in querysets.paginator.page_range:
        if abs(querysets.number - i) < 3:  # display btn
            if querysets.number == i:  # current page
                p_ele = """<span class="layui-laypage-curr"><em class="layui-laypage-em"></em><em>%s</em></span>""" \
                        % i
                # ele += p_ele
            else:
                p_ele = """<a href="?_page=%s" data-page="%s">%s</a>""" % (i, i, i)
            ele += p_ele
    ele += """
    <a href = "?_page=%s" class ="layui-laypage-next %s" data-page="%s">下一页</a>
    </div></div>
    """ % (querysets.number + 1, "layui-disabled" if querysets.number == querysets.paginator.num_pages else '',
           querysets.number + 1)
    return mark_safe(ele)


@register.simple_tag
def get_sorted_column(column, sorted_column, forloop):
    # sorted_column = {'name': '0'}
    if column in sorted_column:  # 这一列被排序了
        # 判断上一次排序是什么顺序，本次取反
        last_sort_index = sorted_column[column]
        if last_sort_index.startswith('-'):
            this_time_sort_index = last_sort_index.strip('-')
        else:
            this_time_sort_index = '-%s' % last_sort_index
        return this_time_sort_index
    return forloop
