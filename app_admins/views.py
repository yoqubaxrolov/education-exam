from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_admins.serializers import  LoginSerializer, RegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_common.permissions import IsSuperAdmin
from django.contrib.auth import get_user_model

User = get_user_model()



class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer 

    def post(self, request):
        serializer = self.serializer_class(data=request.data) 
        serializer.is_valid(raise_exception=True)

        admin = serializer.save()
        raw_password = serializer.validated_data['password']

        admin.set_password(raw_password)
        admin.is_active = True
        admin.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    

class LoginAPIView(APIView):
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        tokens = user.get_tokens() 

        return Response(data=tokens, status=status.HTTP_200_OK)
    
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    
    
class AdminManagementAPIView(APIView):
    permission_classes = [IsSuperAdmin]

    def get(self, request):
        admins = User.objects.filter(role="admin").values("id", "username", "email")
        return Response({"admins": admins}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        admin = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'], role="admin")
        admin.is_staff = True
        admin.save()
        return Response({"message": "Admin created successfully"}, status=status.HTTP_201_CREATED)
    

    




    


        




    

            
            
    
    