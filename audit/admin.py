from django.contrib import admin

# Register your models here.
from audit.models import Model


class ModelAdmin(admin.ModelAdmin):
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
