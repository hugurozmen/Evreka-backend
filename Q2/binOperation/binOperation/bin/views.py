from django.shortcuts import render
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Execution, Bin
# Create your views here.

@api_view(['GET'])
def get_collection_frequency(request):
    execution = Execution.objects.all()
    frequency_list = []
    for execs in execution:
        bin_id = execs.bin_id.id
        frequency = Bin.objects.filter(Q(id=bin_id)).get().collection_frequency
        temp = "The Collection Frequency for the bin which has the id number of " + str(bin_id) + "  is : " + str(frequency)
        frequency_list.append(temp)
    return Response({
        "FrequencyList": frequency_list
    })
