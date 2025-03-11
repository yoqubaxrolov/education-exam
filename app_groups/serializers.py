from rest_framework import serializers

from app_groups.models import Groups, Homeworks

class GroupSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Groups
        fields = ['slug', 'name', 'teacher', 'students']

    def get_students(self, obj):
        return [{'name': student.username} for student in obj.students.all()]
    
    


class HomeworksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homeworks
        fields = ['lesson', 'description', 'homework']

    

    