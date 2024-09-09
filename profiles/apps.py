from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Provides primary key type for profile app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
