from django.apps import AppConfig


class TceEventAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tce_event_app"

    def ready(self):
        import tce_event_app.signals
