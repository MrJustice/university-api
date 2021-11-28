from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'classroom', views.ClassRoomViewSet, basename='classroom')
router.register(r'lesson', views.LessonViewSet, basename='lesson')

urlpatterns = [
    path('', views.api_root),
    path('', include(router.urls)),
    path('schedule/', views.ScheduleList.as_view(), name="get_lessons")
]
