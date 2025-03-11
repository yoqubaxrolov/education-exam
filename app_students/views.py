from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from app_common.permissions import IsAdmin
from app_students.models import Students
from app_students.serializers import StudentsSerializer


class StudentssAPIView(APIView):
    permission_classes = [IsAdmin]
    serializer_class = StudentsSerializer

    def get(self, request):
        students = Students.objects.all()
        serializer = self.serializer_class(students, many=True)
        return Response({"students": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Student created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Something went wrong"})
