from api import models, serializers

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class GroupListView(generics.ListAPIView):
#     queryset = models.Group.objects.all()
#     serializer_class = serializers.GroupSerializer
#
#
# class GroupCreateView(generics.CreateAPIView):
#     queryset = models.Group.objects.all()
#     serializer_class = serializers.GroupSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#
# class GroupDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Group.objects.all()
#     serializer_class = serializers.GroupSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
