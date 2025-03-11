from django.urls import include, path

from app_admins.views import AdminManagementAPIView, LoginAPIView, RegisterAPIView
from rest_framework_simplejwt.views import TokenBlacklistView

app_name = 'admins'

urlpatterns = [
    path('', AdminManagementAPIView.as_view(), name='admin_management'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    # path('create/', TokenBlacklistView.as_view(), name='create_user'),
    # path('teachers/', TokenBlacklistView.as_view(), name='teachers'),
    # path('students/', TokenBlacklistView.as_view(), name='students'),
    
]