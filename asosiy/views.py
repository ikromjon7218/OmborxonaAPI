from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class OmborViewSet(ModelViewSet):
    serializer_class = OmborSerializer
    queryset = Ombor.objects.all()

class MahsulotViewSet(ModelViewSet):
    serializer_class = MahsulotSerializer
    queryset = Mahsulot.objects.all()

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()