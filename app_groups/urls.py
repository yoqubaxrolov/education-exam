from django.urls import path

from app_groups.views import GroupsAPIView, HomeworksAPIView

app_name = 'groups'

urlpatterns = [
    path('', GroupsAPIView.as_view(), name='groups'),
    path('homeworks/', HomeworksAPIView.as_view(), name='homeworks'),
    # path('my_group/', GroupDetailAPIView.as_view(), name='my_group'),
    # path('<str:lesson-title>/homework', GroupDetailAPIView.as_view(), name='my_group'),

    ]
