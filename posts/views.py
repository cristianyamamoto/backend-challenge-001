from rest_framework import viewsets
from rest_framework import permissions
from posts.serializers import PostSerializer
from posts.models import Post
from topics.models import Topic


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        topic = Topic.objects.get(pk=self.request.resolver_match.kwargs['topic_pk'])
        serializer.save(author=self.request.user, topic=topic)