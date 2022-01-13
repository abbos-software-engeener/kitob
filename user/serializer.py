from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer


class RegistrationSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance


class CustomAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if user is not None:
                pass
            else:
                msg = ('Phone or password is incorrect')
                raise ValidationError(msg)
        else:
            msg = ('Must include Phone and password.')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class UserWithPermsSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'perms')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            "first_name": {
                'required': True
            },
            "last_name": {
                'required': True
            }
        }


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=7, max_length=50, error_messages={
            "min_length": _("Parol kamida 7 ta belgidan iborat bo'lishi lozim."),
            "max_length": _("Parol ko'pi bilan 50 ta belgidan iborat bo'lishi mumkin.")
        })
    confirm_password = serializers.CharField(required=True, min_length=7, max_length=50, error_messages={
            "min_length": _("Parol kamida 7 ta belgidan iborat bo'lishi lozim."),
            "max_length": _("Parol ko'pi bilan 50 ta belgidan iborat bo'lishi mumkin.")
        })

    def validate(self, data):
        errors = {}
        if not self.context['request'].user.check_password(data.get('old_password')):
            errors['old_password'] = _("Parol noto'g'ri kiritilgan.")

        if data.get('new_password') != data.get('confirm_password'):
            errors['confirm_password'] = _("Parollar bir xil bo'lishi shart.")

        if data.get('new_password') == data.get('old_password'):
            errors['new_password'] = _("Parol hozirgi parol bilan bir xil.")

        if errors:
            raise serializers.ValidationError(errors)

        return data