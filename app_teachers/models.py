from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel
from app_groups.models import Groups

User = get_user_model()



class Teachers(BaseModel):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='teachers')
    groups = models.ForeignKey('app_groups.Groups', on_delete=models.CASCADE, related_name='teacher_groups')
    students = models.ManyToManyField('app_students.Students',  related_name='teacher_students')

    def __str__(self):
        return self.teacher.username
    
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
    

class Lessons(BaseModel):
    title = models.CharField(max_length=255)
    lesson_vid = models.FileField(upload_to='lessons')
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='group_lesson')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='teacher_lesson')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'




