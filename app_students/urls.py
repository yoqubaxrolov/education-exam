from django.urls import include, path

from app_students.views import StudentssAPIView

app_name = 'students'

urlpatterns = [
    path('', StudentssAPIView.as_view(), name='list'),
    
]