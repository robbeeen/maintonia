from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestModelSerializer

class TestModelCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TestModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
