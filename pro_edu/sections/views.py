from django.shortcuts import render
from .models import Footer,Header
from .serializers import FooterSerializer,HeaderSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class FooterView(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class HeaderView(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
