from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.

# How to stack inline taken from:
#  https://www.youtube.com/watch?v=KNvSWubOaQY


class ProfileInline(admin.StackedInline):
    """
    Stack Profiles inline to User
    """
    model = Profile


class UserAdmin(admin.ModelAdmin):
    """
    Lists fields displayed on admin site
    """
    model = User
    fields = ["username", "password"]
    inlines = [ProfileInline]


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
