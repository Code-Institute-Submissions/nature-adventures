from django.apps import AppConfig


class HikesConfig(AppConfig):
    """
    Provides primary key type for hike app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hikes'
