from datetime import datetime, timedelta

from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from records.serializers import NavigationRecordListSerializer

from records.models import NavigationRecord
from rest_framework.response import Response


# @api_view(['GET'])
# def get_last_points(request):
#     today = datetime.now()
#     two_days_ago = today - timedelta(days=2)
#     orders = NavigationRecord.objects.filter(Q(datetime__gte=two_days_ago)).values()
#     print(orders)
#     return Response({
#         'last_points': orders
#     })
# That's an option


class NavigationRecordListAPIView(ListAPIView):
    serializer_class = NavigationRecordListSerializer

    def get_queryset(self):
        today = datetime.now()
        two_days_ago = today - timedelta(days=2)
        return NavigationRecord.objects.filter(Q(datetime__gte=two_days_ago))
