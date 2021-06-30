"""
API V1: Comments Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from comments.models import Comment


###
# Serializers
###
class CreateCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'created_at',
            'updated_at',
            'title',
            'content'
        )


class RetrieveCommentSerializer(CreateCommentSerializer):
    post = serializers.ReadOnlyField(source='post.title')
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta(CreateCommentSerializer.Meta):
        model = Comment
        fields = CreateCommentSerializer.Meta.fields + (
            'post',
            'author'
        )
        read_only_fields = fields

    
class NestedCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author')