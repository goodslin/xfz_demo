from heroadmin.admin_base import BaseHeroAdmin


class AdminSite(object):
    def __init__(self):
        self.enabled_admin = {}

    def register(self, model_class, admin_class=None):
        """注册admin表"""

        print("register", model_class, admin_class)
        app_name = model_class._meta.app_label
        model_name = model_class._meta.model_name

        if not admin_class:
            admin_class = BaseHeroAdmin()
        else:
            admin_class = admin_class()
        admin_class.model = model_class     # 把modelclass赋值给了admin_class
        if app_name not in self.enabled_admin:
            self.enabled_admin[app_name] = {}
        self.enabled_admin[app_name][model_name] = admin_class


site = AdminSite()
