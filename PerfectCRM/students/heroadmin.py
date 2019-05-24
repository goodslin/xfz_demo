from heroadmin.sites import site
from students import models
from heroadmin.admin_base import BaseHeroAdmin

print('student heroadmin......')


class TestAdmin(BaseHeroAdmin):
    list_display = ['name']


site.register(models.Test, TestAdmin)
