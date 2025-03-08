from rest_framework import serializers

from app_groups.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['slug', ]