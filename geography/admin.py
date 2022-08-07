from django.contrib import admin
from django.utils.text import slugify

from geography.models import Country


class CountryAdmin(admin.ModelAdmin):
    """admin for country"""

    list_display = ["name", "slug", "iso2", "iso3", "phone_code", "archived"]
    list_editable = ("archived",)
    readonly_fields = [
        "id",
        "slug",
    ]
    search_fields = ["id", "name", "slug", "iso2", "iso3", "phone_code"]
    ordering = ["name"]
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "id",
                    "name",
                    "slug",
                    "iso2",
                    "iso3",
                    "phone_code",
                    "archived",
                ]
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change and Country.objects.filter(slug=slugify(obj.name)).exists():
            raise Exception("Country with this name already exists")
        else:
            obj._user_agent = request.META["HTTP_USER_AGENT"]
            obj._remote_addr = request.META["REMOTE_ADDR"]
            obj._account = request.user
            super().save_model(request, obj, form, change)


admin.site.register(Country, CountryAdmin)
