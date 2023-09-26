from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from api.models import User, WorkExperience, Studies, School, Company, Courses
from rest_framework import status
from django.http import Http404

# Create your views here.
class User_APIView(APIView):
    def get(self, request,format=None, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)