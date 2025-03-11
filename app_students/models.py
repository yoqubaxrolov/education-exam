from django.db import models
from django.contrib.auth import get_user_model
from app_common.models import BaseModel 


User = get_user_model()

class Students(BaseModel):
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='students')
    group = models.ForeignKey('app_groups.Groups', on_delete=models.DO_NOTHING, related_name='student_group')
    teacher = models.ForeignKey('app_teachers.Teachers', on_delete=models.CASCADE, related_name='students_teacher')
    homeworks = models.ManyToManyField('app_groups.Homeworks', related_name='homeworks')

    def __str__(self):
        return self.student.username
    
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'