from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_common.permissions import IsAdmin, IsStudent, IsTeacher
from django.contrib.auth import get_user_model

from app_groups.models import Groups, Homeworks
from app_groups.serializers import GroupSerializer, HomeworksSerializer

User = get_user_model()

class GroupsAPIView(APIView):
    permission_classes = [IsAdmin] 
    serializer_class = GroupSerializer

    def get(self, request):
        groups = Groups.objects.all()
        serializer = self.serializer_class(groups, many=True)
        return Response({"groups": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print('salom')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('xayr')
            serializer.save()
            return Response({"message": "Group created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Something went wrong"})


class HomeworksAPIView(APIView):
    permission_classes = [IsTeacher or IsStudent] 
    serializer_class = HomeworksSerializer

    def get(self, request):
        homeworks = Homeworks.objects.all()
        serializer = self.serializer_class(homeworks, many=True)
        return Response({"homeworks": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Homework added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Something went wrong"})