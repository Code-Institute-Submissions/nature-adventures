from django.contrib import admin
from .models import Hike

# Register your models here.

class HikeAdmin(admin.ModelAdmin):
    list_display = ("hike_name", "region", "distance", "author", "description", "route_image",)
    prepopulated_fields = {"slug": ("hike_name",)}

admin.site.register(Hike, HikeAdmin)