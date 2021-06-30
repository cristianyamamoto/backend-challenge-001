"""
API V1: Posts Views
"""
###
# Libraries
###
from rest_framework import viewsets
from rest_framework import permissions
from posts.api.v1.serializers import *
from posts.models import Post
from topics.models import Topic
from helpers.permissions import IsOwnerOrReadOnly

###
# Filters
###


###
# Viewsets
###
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        topic = Topic.objects.get(url_name=self.kwargs['topic_url_name'])
        serializer.save(author=self.request.user, topic=topic)
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreatePostSerializer
        return RetrievePostSerializer
