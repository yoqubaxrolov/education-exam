from rest_framework import serializers
from django.contrib.auth import get_user_model

from app_groups.models import Groups
from app_teachers.models import Lessons, Teachers

User = get_user_model()

class TeachersSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField()
    groups = serializers.CharField() 
    students = serializers.SerializerMethodField() 

    class Meta:
        model = Teachers
        fields = ['teacher', 'groups', 'students']

    def create(self, validated_data):
        username = validated_data.pop('teacher')  
        teacher = User.objects.filter(username=username, role='teacher').first()
        if not teacher:
            raise serializers.ValidationError({"teacher": "Teacher not found or invalid role."})

        group_name = validated_data.pop('groups')
        group = Groups.objects.filter(name=group_name).first()
        if not group:
            raise serializers.ValidationError({"groups": "Group not found."})

        validated_data['teacher'] = teacher
        validated_data['groups'] = group
        teacher = Teachers.objects.create(**validated_data)
        return teacher 

    def get_students(self, obj):
        return [student.username for student in obj.students.all()]  # Studentlar username ro‘yxati





        
class LessonsSerializer(serializers.ModelSerializer):
    groups = serializers.CharField()

    class Meta:
        model = Lessons
        fields = ['title', 'lesson_vid', 'group', 'teacher']
        


