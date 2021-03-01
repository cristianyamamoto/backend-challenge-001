from rest_framework import viewsets
from rest_framework import permissions
from comments.serializers import *
from comments.models import Comment
from posts.models import Post
from helpers.permissions import IsOwnerOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.request.resolver_match.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateCommentSerializer
        return RetrieveCommentSerializer