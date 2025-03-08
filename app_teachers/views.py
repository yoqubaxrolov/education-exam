from django.shortcuts import render
from rest_framework.views import APIView


class TeachersListView(APIView):
    def get(self, request):
        return render(request, 'teachers/list.html')
    


