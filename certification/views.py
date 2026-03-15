from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .models import Certification
from .serializers import CertificationSerializer


class CertificationListCreateAPIView(APIView):

    def get(self, request):

        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=CertificationSerializer)
    def post(self, request):

        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CertificationDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            return None


    def get(self, request, pk):

        certification = self.get_object(pk)

        if certification is None:
            return Response(
                {"error": "Certification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CertificationSerializer(certification)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=CertificationSerializer)
    def put(self, request, pk):

        certification = self.get_object(pk)

        if certification is None:
            return Response(
                {"error": "Certification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CertificationSerializer(certification, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=CertificationSerializer)
    def patch(self, request, pk):

        certification = self.get_object(pk)

        if certification is None:
            return Response(
                {"error": "Certification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CertificationSerializer(
            certification,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        certification = self.get_object(pk)

        if certification is None:
            return Response(
                {"error": "Certification not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        certification.delete()

        return Response(
            {"message": "Certification deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
