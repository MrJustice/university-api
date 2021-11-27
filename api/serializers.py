from api import models
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()

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
    classroom = ClassRoomSerializer(read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = models.Lesson
        fields = "__all__"
