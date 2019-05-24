from django.contrib import admin
from crm01 import models


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'source', 'contact_type', 'contact', 'consultant', 'consult_content', 'status',
                    'date']
    list_filter = ['source', 'consultant', 'date']
    search_fields = ['contact', 'consultant__name']


admin.site.register(models.UserProfile)
admin.site.register(models.Role)
admin.site.register(models.CustomeInfo, CustomerAdmin)
admin.site.register(models.Student)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyReocrd)
admin.site.register(models.Branch)
admin.site.register(models.Menus)
