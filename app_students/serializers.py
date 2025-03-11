from rest_framework import serializers
from django.contrib.auth import get_user_model

from app_students.models import Students

User = get_user_model()

class StudentsSerializer(serializers.ModelSerializer):
    group = serializers.CharField(required=False)

    class Meta:
        model = Students
        fields = ['group', 'teacher']
        


        



