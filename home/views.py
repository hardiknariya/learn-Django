from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from home import models


# Create your views here.


def index(request):
    return render(request, 'home.html')


class StudentCreate(generics.CreateAPIView):
    serializer_class = StudentSerializer
    model = models.Student
    queryset = models.Student.objects.all()

    def perform_create(self, serializer):
        serializer.save()
