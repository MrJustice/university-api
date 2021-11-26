from api import models, serializers

from rest_framework import viewsets


class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = models.ClassRoom.objects.all()
    serializer_class = serializers.ClassRoomSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
