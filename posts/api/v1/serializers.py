"""
API V1: Posts Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from posts.models import Post
from comments.api.v1.serializers import NestedCommentSerializer
from comments.models import Comment


###
# Serializers
###
class CreatePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'content'
        )


class RetrievePostSerializer(CreatePostSerializer):
    topic = serializers.ReadOnlyField(source='topic.url_name')
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.SerializerMethodField()
    
    class Meta(CreatePostSerializer.Meta):
        model = Post
        fields = CreatePostSerializer.Meta.fields + (
            'topic',
            'author',
            'comments'
        )
        read_only_fields = fields

    def get_comments(self, instance):
        return NestedCommentSerializer(
            Comment.objects.filter(post=instance).order_by('-updated_at')[:5],
            many=True
        ).data


class NestedPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'author')