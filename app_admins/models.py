from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUserModel(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)  # Default student
    
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)
    
    def get_tokens(self):
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(self)
        refresh['role'] = self.role  # Token ichiga role qo‘shamiz
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': self.role
        }
    

    
























