from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from .serializers import UserRegisterSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import logging


logger = logging.getLogger(__file__)

User = get_user_model()

class CustomBackend:
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username) | Q(
                mobile=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 验证合法
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = make_password(serializer.validated_data['password'])
        email = serializer.validated_data['email']

        user = User(username=username, password=password, email=email, is_staff=True)
        user.save()

        return Response({
            "username": username,
            "email": email,
            "password": password,
        }, status=status.HTTP_201_CREATED)
