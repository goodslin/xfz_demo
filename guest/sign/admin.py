from django.contrib import admin
from sign.models import Event
from sign.models import Guest


# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'address', 'start_time',)
    search_fields = ('name',)  # 搜索栏
    list_filter = ('status',)  # 过滤器


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('realname', 'phone', 'email', 'sign', 'create_time', 'event',)
    search_fields = ('realname', 'phone',)  # 搜索栏
    list_filter = ('sign',)  # 过滤器


