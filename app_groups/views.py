from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_common.permissions import IsAdmin
from django.contrib.auth import get_user_model

from app_groups.models import Group

User = get_user_model()

class GroupsManagementAPIView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        groups = Group.objects.all()
        return Response({"groups": groups}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        group = Group.objects.create(name=data['name'], students=data['students'.count], password=data['teacher'])
        group.save()
        return Response({"message": "Group created successfully"}, status=status.HTTP_201_CREATED)
