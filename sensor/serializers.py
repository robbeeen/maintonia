from .models import TestModel
from rest_framework import serializers

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'
