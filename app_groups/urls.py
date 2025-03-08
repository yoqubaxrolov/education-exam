from django.urls import path

from app_groups.views import GroupsManagementAPIView

app_name = 'groups'

urlpatters = [
    path('groups/', GroupsManagementAPIView.as_view(), name='groups'),
    # path('my_group/', GroupDetailAPIView.as_view(), name='my_group'),
    # path('<str:lesson-title>/homework', GroupDetailAPIView.as_view(), name='my_group'),

    ]
