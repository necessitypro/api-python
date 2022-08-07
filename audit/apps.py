from django.apps import AppConfig


class AuditConfig(AppConfig):
    """config for audit"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "audit"
