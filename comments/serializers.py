from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.title')
    
    class Meta:
        model = Comment
        fields = ['created_at', 'updated_at', 'title',
                  'content', 'post', 'author']
