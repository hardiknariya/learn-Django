from django.shortcuts import render
from rest_framework import generics
from account import serializers , models
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator

sensitive_post_method = sensitive_post_parameters('password')


class Index(generics.ListAPIView):
    serializer_class = serializers.ListUserSerializer
    models = get_user_model()
    queryset = models.objects.all()

    def get_queryset(self):
        return self.queryset.filter()


@method_decorator(sensitive_post_method, name='dispatch')
class UserRegister(generics.CreateAPIView):
    serializer_class = serializers.SignUpSerializer
    models = get_user_model()
    queryset = models.objects.all()
    # permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.generate_auth_token()

        return Response(serializer.get_data())

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['url_params'] = self.kwargs
        return context


@method_decorator(sensitive_post_method, name='dispatch')
class UserLogin(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_data())
