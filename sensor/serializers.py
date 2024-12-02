from .models import SensorReading
from rest_framework import serializers

class SensorReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'
