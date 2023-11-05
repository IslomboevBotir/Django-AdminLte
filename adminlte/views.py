from django.shortcuts import render
from rest_framework.views import APIView
from .models import AxCoreLeadsModel
# Create your views here.


def index(request):
    return render(request, 'adminlte/index.html')


class AxCoreLeads(APIView):
    def get(self, request):
        query = AxCoreLeadsModel.objects.all()
        return render(request, 'adminlte/index.html', {'query': query})
