from rest_framework import serializers
from api.models import User, WorkExperience, Studies, School, Company, Courses


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        exclude = ['create_at','update_at']