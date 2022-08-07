from django.contrib import admin

from authentication.models import Account


class AccountAdmin(admin.ModelAdmin):
    """admin for account"""

    list_display = [
        "email",
        "full_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "phone_verified",
        "date_joined",
    ]

    list_editable = [
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "phone_verified",
    ]

    fieldsets = (
        ("Name", {"fields": ("first_name", "last_name")}),
        ("Email", {"fields": ("email", "email_verified", "email_verified_on")}),
        (
            "Phone",
            {
                "fields": (
                    "phone",
                    "phone_verified",
                    "phone_verified_on",
                    "phone_one_time_code",
                )
            },
        ),
        ("Access", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Groups", {"fields": ("groups",)}),
        ("Permissions", {"fields": ("user_permissions",)}),
        ("Secret", {"fields": ("password", "token")}),
    )

    readonly_fields = (
        "token",
        "email_verified_on",
        "date_joined",
        "last_login",
        "password",
        "phone_verified_on",
        "phone_one_time_code",
    )

    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "groups",
        "date_joined",
    ]

    date_hierarchy = "date_joined"

    @staticmethod
    def full_name(obj):
        """return full name"""
        return f"{obj.first_name} {obj.last_name}"


admin.site.register(Account, AccountAdmin)
