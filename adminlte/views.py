from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import AxCoreLeadsModel
from .serializer import AxCoreLeadsSerializer
# Create your views here.


def index(request):
    return render(request, 'adminlte/index.html')


class AxCoreLeads(APIView):
    def get(self, request):
        query = AxCoreLeadsModel.objects.all()
        serializer = AxCoreLeadsSerializer(query, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)
