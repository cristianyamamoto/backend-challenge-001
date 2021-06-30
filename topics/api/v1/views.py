"""
API V1: Topics Views
"""
###
# Libraries
###
from rest_framework import viewsets
from rest_framework import permissions
from topics.api.v1.serializers import *
from topics.models import Topic
from helpers.permissions import IsOwnerOrReadOnly


###
# Filters
###


###
# Viewsets
###
class TopicViewSet(viewsets.ModelViewSet):
    lookup_field = 'url_name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Topic.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateTopicSerializer
        return RetrieveTopicSerializer