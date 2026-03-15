from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Get all vendor product mappings"
    )
    def get(self, request):

        mappings = VendorProductMapping.objects.all()

        vendor_id = request.GET.get("vendor_id")

        if vendor_id:
            mappings = mappings.filter(vendor_id=vendor_id)

        serializer = VendorProductMappingSerializer(mappings, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Create vendor product mapping",
        request_body=VendorProductMappingSerializer
    )
    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VendorProductMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return VendorProductMapping.objects.get(pk=pk)
        except VendorProductMapping.DoesNotExist:
            return None


    @swagger_auto_schema(
        operation_description="Get vendor product mapping by ID"
    )
    def get(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorProductMappingSerializer(mapping)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Update vendor product mapping",
        request_body=VendorProductMappingSerializer
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorProductMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Partially update vendor product mapping",
        request_body=VendorProductMappingSerializer
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorProductMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete vendor product mapping"
    )
    def delete(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        mapping.delete()

        return Response(
            {"message": "Mapping deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
