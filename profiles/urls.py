from . import views
from django.urls import path

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('profiles/update_profile/', views.update_profile, name='update_profile'),
]