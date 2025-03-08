from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel
from app_teachers.models import Lesson

User = get_user_model()

class Group(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='teacher') 
    students = models.ManyToManyField(User, limit_choices_to={'role': 'student'}, related_name="students")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'


class Homework(BaseModel):
    lesson = models.ForeignKey("app_teachers.Lesson", on_delete=models.CASCADE, related_name='lesson')
    description = models.TextField()
    homework = models.FileField(upload_to='homeworks', null=True)
    
    def __str__(self):
        return f"{self.lesson.title}"
    
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
