from django.contrib import admin

from audit.models import Model


class ModelAdmin(admin.ModelAdmin):
    """admin for model"""

    readonly_fields = (
        "id",
        "operation",
        "timestamp",
        "account",
        "data_type",
        "data_id",
        "data",
        "user_agent",
        "remote_addr",
    )


admin.site.register(Model, ModelAdmin)
