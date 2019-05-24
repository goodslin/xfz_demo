from heroadmin import sites
from crm01 import models
from heroadmin.admin_base import BaseHeroAdmin

print('crm01 heroadmin....')


class CustomerAdmin(BaseHeroAdmin):
    list_display = ['id', 'name', 'source', 'contact_type', 'contact', 'consultant', 'consult_content', 'status',
                    'date']
    list_filter = ['source', 'consultant', 'status', 'date']
    search_fields = ['contact', 'consultant__name']


sites.site.register(models.CustomeInfo, CustomerAdmin)
sites.site.register(models.Role)
sites.site.register(models.Menus)
sites.site.register(models.UserProfile)
sites.site.register(models.CustomerFollowUp)
sites.site.register(models.Course)
sites.site.register(models.CourseRecord)
sites.site.register(models.StudyReocrd)
