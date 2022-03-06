from rest_framework import serializers
from home import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
        read_only_fields = ('id')
