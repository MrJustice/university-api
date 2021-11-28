import datetime
from api import models, serializers
from rest_framework import viewsets, status, permissions, generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request):
    return Response({
        'Groups': reverse('group-list', request=request),
        'Classrooms': reverse('classroom-list', request=request),
        'Students': reverse('student-list', request=request),
        'Lessons': reverse('lesson-list', request=request),
        'Endpoint': "http://0.0.0.0:8000/api/schedule/?group_name=Group_1&date=29-11-2021",
    })


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


class ScheduleList(generics.ListAPIView):
    serializer_class = serializers.LessonSerializer

    def get_queryset(self):
        group_name = self.request.query_params.get("group_name")
        date = self.request.query_params.get("date")
        date = datetime.datetime.strptime(date, "%d-%m-%Y")
        queryset = models.Lesson.objects.filter(
            start_at__range=[
                datetime.datetime.combine(date, datetime.time.min),
                datetime.datetime.combine(date, datetime.time.max)
            ],
            group__name=group_name
        )
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
