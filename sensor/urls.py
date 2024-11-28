from django.urls import path
from .views import TestModelCreateView

urlpatterns = [
    path('testmodel/', TestModelCreateView.as_view(), name='testmodel-create'),
]