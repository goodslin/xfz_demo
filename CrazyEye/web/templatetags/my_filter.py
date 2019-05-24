from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def time_line(value):
    if not isinstance(value, datetime):
        return value
    now = datetime.now()
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif timestamp >= 60 and timestamp < 60 * 60:
        minutes = int(timestamp / 60)
        return "%s分钟前" % minutes
    elif timestamp >= 60 * 60 and timestamp < 60 * 60 * 24:
        hours = int(timestamp / 60 / 60)
        return "%s小时前" % hours
    elif timestamp >= 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
        days = int(timestamp / 60 / 60 / 24)
        return "%s天前" % days
    else:
        return value.strftime("%Y/%m/%d %H:%M")
