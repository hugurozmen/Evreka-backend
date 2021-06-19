from django.urls import path
from .views import get_collection_frequency
urlpatterns = [
    path('frequency/', get_collection_frequency)
]
