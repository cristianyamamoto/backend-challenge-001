from rest_framework import viewsets
from rest_framework import permissions
from posts.serializers import *
from posts.models import Post
from topics.models import Topic
from helpers.permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        topic = Topic.objects.get(url_name=self.kwargs['topic_url_name'])
        serializer.save(author=self.request.user, topic=topic)
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreatePostSerializer
        return RetrievePostSerializer