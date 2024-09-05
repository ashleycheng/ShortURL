from django.contrib import admin
from .models import URLMapping


class URLMappingAdmin(admin.ModelAdmin):
    readonly_fields = (
        "short_url",
        "expiration_date",
    )
    list_display = (
        "short_url",
        "expiration_date",
    )


admin.site.register(URLMapping, URLMappingAdmin)
