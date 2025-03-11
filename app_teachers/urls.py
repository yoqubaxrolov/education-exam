from django.urls import include, path

from app_teachers.views import LessonsAPIView, TeachersAPIView

app_name = 'teachers'

urlpatterns = [
    path('', TeachersAPIView.as_view(), name='teachers-list'),
    path('lessons/', LessonsAPIView.as_view(), name='lessons-list'),
    
]