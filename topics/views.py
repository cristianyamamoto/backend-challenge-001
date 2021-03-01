from rest_framework import viewsets
from rest_framework import permissions
from topics.serializers import *
from topics.models import Topic
from helpers.permissions import IsOwnerOrReadOnly

class TopicViewSet(viewsets.ModelViewSet):

    queryset = Topic.objects.all()
    lookup_field = 'url_name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateTopicSerializer
        return RetrieveTopicSerializer