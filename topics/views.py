from rest_framework import viewsets
from rest_framework import permissions
from topics.serializers import TopicSerializer
from topics.models import Topic


class TopicViewSet(viewsets.ModelViewSet):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'url_name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)