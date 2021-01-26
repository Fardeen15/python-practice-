from rest_framework import serializers
from .models import Student, StudentClass
from django.contrib.auth.models import User


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class NewUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email',"is_superuser"]


class StudentSerializer1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'firstname', 'lastname', 'number', 'grade']


class StudentClassSerializer(serializers.HyperlinkedModelSerializer):
    # studentName = StudentSerializer1(many=False, read_only=True)

    class Meta:
        model = StudentClass
        fields = ['id', 'studentclass', 'studentName', ]

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('studentName')
    #     album = StudentClass.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         StudentClass.objects.create(album=album, **track_data)
    #     return album
