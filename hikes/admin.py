from django.contrib import admin
from .models import Hike

# Register your models here.

class HikeAdmin(admin.ModelAdmin):
    """
    Shows the fields displayed on admin site
    """

    list_display = (
        "hike_name",
        "region",
        "distance",
        "author",
        "description",
        "route_image",
        )
    prepopulated_fields = {"slug": ("hike_name",)}

# Register the Hike Model
admin.site.register(Hike, HikeAdmin)