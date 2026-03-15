from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .models import Course
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):

    def get(self, request):

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=CourseSerializer)
    def post(self, request):

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CourseDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None


    def get(self, request, pk):

        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=CourseSerializer)
    def put(self, request, pk):

        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=CourseSerializer)
    def patch(self, request, pk):

        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        course.delete()

        return Response(
            {"message": "Course deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
