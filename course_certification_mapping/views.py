from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Get all course certification mappings"
    )
    def get(self, request):

        mappings = CourseCertificationMapping.objects.all()

        course_id = request.GET.get("course_id")

        if course_id:
            mappings = mappings.filter(course_id=course_id)

        serializer = CourseCertificationMappingSerializer(mappings, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Create course certification mapping",
        request_body=CourseCertificationMappingSerializer
    )
    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None


    @swagger_auto_schema(
        operation_description="Get course certification mapping by ID"
    )
    def get(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseCertificationMappingSerializer(mapping)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Update course certification mapping",
        request_body=CourseCertificationMappingSerializer
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Partially update course certification mapping",
        request_body=CourseCertificationMappingSerializer
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseCertificationMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete course certification mapping"
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
