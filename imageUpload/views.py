from django.shortcuts import render
from .models import AdImage
from .serializers import ImageSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.http import HttpResponse

class ImageView(viewsets.ModelViewSet):
    queryset = AdImage.objects.all()
    serializer_class = ImageSerializer
