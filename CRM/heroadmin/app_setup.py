from django import conf


def heroadmin_auto_discover():

    for app_name in conf.settings.INSTALLED_APPS:
        try:
            mod = __import__("%s.heroadmin" % app_name)
            print(mod.heroadmin)
        except ImportError:
            pass
