from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'classroom', views.ClassRoomViewSet, basename='classroom')
router.register(r'lesson', views.LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
]
