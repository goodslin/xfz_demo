from heroadmin.sites import site
from heroadmin.admin_base import BaseKingAdmin
from crm import models

print('crm heroadmin ............')


class CustomerAdmin(BaseKingAdmin):
    list_display = ['name', 'source', 'contact_type', 'contact', 'consultant', 'consult_content', 'status', 'date']
    list_filter = ['source', 'consultant', 'status', 'date']
    search_fields = ['contact', 'consultant__name']


site.register(models.CustomerInfo, CustomerAdmin)
site.register(models.Role)
site.register(models.Menus)
site.register(models.UserProfile)
