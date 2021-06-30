"""
API V1: Topics Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from topics.models import Topic
from posts.api.v1.serializers import NestedPostSerializer
from posts.models import Post


###
# Serializers
###
class CreateTopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'name',
            'description',
            'url_name'
        )


class RetrieveTopicSerializer(CreateTopicSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    posts = serializers.SerializerMethodField()

    class Meta(CreateTopicSerializer.Meta):
        model = Topic
        fields = CreateTopicSerializer.Meta.fields + (
            'author',
            'posts'
        )
        read_only_fields = fields

    def get_posts(self, instance):
        return NestedPostSerializer(
            Post.objects.filter(topic=instance).order_by('-updated_at')[:5],
            many=True
        ).data
