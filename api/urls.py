from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groups', views.GroupViewSet, basename='group')
urlpatterns = [
    # path("group/list/", views.GroupListView.as_view(), name="group_list"),
    # path("group/detail/<int:group_id>/", views.GroupDetailsView.as_view(), name="group_detail"),
    # path("group/create/", views.GroupCreateView.as_view(), name="group_create"),
    path('', include(router.urls)),
]
