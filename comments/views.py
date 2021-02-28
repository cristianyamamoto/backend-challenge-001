from rest_framework import viewsets
from rest_framework import permissions
from comments.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.request.resolver_match.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)