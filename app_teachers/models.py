from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel

User = get_user_model()



class Lesson(BaseModel):
    title = models.CharField(max_length=255)
    lesson_vid = models.FileField(upload_to='lessons')
    group = models.ForeignKey('app_groups.Group', on_delete=models.CASCADE, related_name='group')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')  # Faqat teacher

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'




