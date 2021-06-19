from django.urls import path

from .views import *

app_name = "post"

urlpatterns = [
    # path('lastpoints', get_last_points, name='latest'),
    path('lastpoints', NavigationRecordListAPIView.as_view(), name='list'),
]
