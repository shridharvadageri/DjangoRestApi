from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Allotment
from .serializers import AllotmentSerializer

class LaptopAllotmentPerformView(APIView):
    def post(self, request):
        serializer = AllotmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Allotment successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
