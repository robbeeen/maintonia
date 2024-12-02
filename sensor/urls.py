from django.urls import path
from .views import SensorReadingCreateView

urlpatterns = [
    path('sensor_reading/', SensorReadingCreateView.as_view(), name='sensor-create'),
]