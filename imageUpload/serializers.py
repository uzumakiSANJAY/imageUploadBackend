from rest_framework import serializers
from .models import  AdImage 

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = '__all__'