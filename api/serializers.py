from api import models
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=models.Group.objects.all())

    class Meta:
        model = models.Student
        fields = "__all__"


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassRoom
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    lessons = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Group
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=models.ClassRoom.objects.all())
    group = serializers.PrimaryKeyRelatedField(queryset=models.Group.objects.all())

    class Meta:
        model = models.Lesson
        fields = "__all__"
