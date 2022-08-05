from django.contrib import admin

from authentication.models import Account

# django admin for account
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
        "email_verified",
    ]

    list_editable = ["is_active", "is_staff", "is_superuser", "email_verified"]

    fieldsets = (
        ("Name", {"fields": ("first_name", "last_name")}),
        ("Email", {"fields": ("email", "email_verified", "email_verified_on")}),
        ("Access", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Groups", {"fields": ("groups",)}),
        ("Permissions", {"fields": ("user_permissions",)}),
        ("Secret", {"fields": ("password", "token")}),
    )

    readonly_fields = ("token", "email_verified_on", "date_joined", "last_login")

    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "groups",
        "date_joined",
    ]

    date_hierarchy = "date_joined"


admin.site.register(Account, AccountAdmin)
