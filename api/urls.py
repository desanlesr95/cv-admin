from django.urls import path
from .views import User_APIView

urlpatterns = [
    path('users', User_APIView.as_view(), name='user-list'),
]