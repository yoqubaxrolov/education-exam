from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from app_common.permissions import IsAdmin, IsTeacher
from app_teachers.models import Lessons, Teachers
from app_teachers.serializers import LessonsSerializer, TeachersSerializer




class TeachersAPIView(APIView):
    permission_classes = [IsAdmin]
    serializer_class = TeachersSerializer

    def get(self, request):
        teachers = Teachers.objects.all()
        serializer = self.serializer_class(teachers, many=True)
        return Response({"teachers": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Teacher created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Something went wrong"})
    

class LessonsAPIView(APIView):
    permission_classes = [IsAdmin or IsTeacher]
    serializer_class = LessonsSerializer

    def get(self, request):
        lessons = Lessons.objects.all()
        serializer = self.serializer_class(lessons, many=True)
        return Response({"lessons": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Lesson added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Something went wrong"})


        
        
    


