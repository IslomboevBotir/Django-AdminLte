from rest_framework import serializers
from .models import AxCoreLeadsModel


class AxCoreLeadsSerializer(serializers.Serializer):
    class Meta:
        model = AxCoreLeadsModel
        fields = '__all__'
