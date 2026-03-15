from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Get all product course mappings"
    )
    def get(self, request):

        mappings = ProductCourseMapping.objects.all()

        product_id = request.GET.get("product_id")

        if product_id:
            mappings = mappings.filter(product_id=product_id)

        serializer = ProductCourseMappingSerializer(mappings, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Create product course mapping",
        request_body=ProductCourseMappingSerializer
    )
    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return ProductCourseMapping.objects.get(pk=pk)
        except ProductCourseMapping.DoesNotExist:
            return None


    @swagger_auto_schema(
        operation_description="Get product course mapping by ID"
    )
    def get(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductCourseMappingSerializer(mapping)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Update product course mapping",
        request_body=ProductCourseMappingSerializer
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Partially update product course mapping",
        request_body=ProductCourseMappingSerializer
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductCourseMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete product course mapping"
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
