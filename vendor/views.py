from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreateAPIView(APIView):

    def get(self, request):

        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=VendorSerializer)
    def post(self, request):

        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VendorDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return None


    def get(self, request, pk):

        vendor = self.get_object(pk)

        if vendor is None:
            return Response(
                {"error": "Vendor not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorSerializer(vendor)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=VendorSerializer)
    def put(self, request, pk):

        vendor = self.get_object(pk)

        if vendor is None:
            return Response(
                {"error": "Vendor not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=VendorSerializer)
    def patch(self, request, pk):

        vendor = self.get_object(pk)

        if vendor is None:
            return Response(
                {"error": "Vendor not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorSerializer(vendor, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        vendor = self.get_object(pk)

        if vendor is None:
            return Response(
                {"error": "Vendor not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        vendor.delete()

        return Response(
            {"message": "Vendor deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
