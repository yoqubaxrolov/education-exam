from django.apps import AppConfig


class AppGroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_groups'

    def ready(self):
        import app_groups.signals
