from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.mixins import UserSerializer
from account import models
import uuid
from datetime import datetime
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')


class SignUpSerializer(UserSerializer, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

        read_only_fields = ('is_superuser',
                            'is_active', 'date_joined', 'username', 'last_login', 'groups', 'user_permissions',
                            'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        validated_data['username'] = uuid.uuid4().hex[:50]
        user = get_user_model().objects.create_user(**validated_data)
        self.user = user
        return user


class LoginSerializer(UserSerializer, serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True, required=True, error_messages=dict(
        required="Password field may not be blank."))

    username = serializers.CharField(max_length=250, write_only=True, required=True, error_messages=dict(
        required="UserName may not be blank."))

    # business = serializers.IntegerField(write_only=True, required=True, error_messages=dict(
    #     required="Business ID may not be blank."))

    class Meta:
        model = get_user_model()
        fields = ('username', "password")

    def validate(self, data):
        try:
            user = get_user_model().objects.get(Q(email__iexact=data.get('username')))
            print("user", user)
            if not user:
                raise AuthenticationFailed(detail='Invalid username or password')

            if not user.check_password(data.get('password')):
                raise AuthenticationFailed(detail='Invalid username or password')

            user.last_login = datetime.now()
            user.save(update_fields=['last_login'])
            self.user = user
            self.generate_auth_token()
            return user

        except get_user_model().DoesNotExist:
            raise AuthenticationFailed()
