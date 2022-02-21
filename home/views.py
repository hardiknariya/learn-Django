from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from home import models
from rest_framework.permissions import IsAuthenticated


# Create your views here.


def index(request):
    return render(request, 'home.html')


class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer
    models = models.Student
    queryset = models.objects.all()

    def get_queryset(self):
        return self.queryset.filter()


class StudentCreate(generics.CreateAPIView):
    serializer_class = StudentSerializer
    models = models.Student
    queryset = models.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class StudentUpdate (generics.UpdateAPIView):
    serializer_class = StudentSerializer
    models = models.Student
    queryset = models.objects.all()
    http_method_names = ['patch']
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])


class StudentDelete(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = models.Student.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])
