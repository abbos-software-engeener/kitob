from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import User
from .serializer import *
from user.responses import ResponseFail, ResponseSuccess
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import password_changed
from .filters import UserSearchFilter


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)


class UserLogin(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user, many=False)
            resp = {
                **serializer.data,
                "token": token.key,
            }
            return ResponseSuccess(resp)
        else:
            return ResponseFail(serializer.errors)


class MeView(APIView):
    """
    Foydalanuvchi haqida ma'lumot qaytaradi
    """
    def get(self, request):
        return ResponseSuccess({
            "user": UserWithPermsSerializer(request.user).data
        })


class ProfileView(APIView):
    """
    Foydalanuvchi ma'lumotlarini tahrirlaydi
    """
    def post(self, request):
        profile = ProfileSerializer(instance=request.user, data=request.data)
        if not profile.is_valid():
            return ResponseFail(profile.errors)

        profile.save()

        return ResponseSuccess({
            "user": profile.data
        })


class ChangePasswordView(APIView):
    """
    Foydalanuvchini parolni o'zgartiradi
    """
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return ResponseFail(serializer.errors)

        user.set_password(serializer.validated_data.get("new_password"))
        user.save()

        password_changed(serializer.validated_data['new_password'], request.user)

        return ResponseSuccess()


class SearchUserView(ListAPIView):

    field = "users"
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = None
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = UserSearchFilter

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)[:10]