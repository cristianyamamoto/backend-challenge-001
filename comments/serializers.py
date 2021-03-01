from rest_framework import serializers
from comments.models import Comment
from rest_auth.serializers import UserDetailsSerializer


class CreateCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['created_at', 'updated_at', 'title',
                  'content']

class RetrieveCommentSerializer(serializers.ModelSerializer):
    
    author = UserDetailsSerializer(read_only=True)
    post = serializers.ReadOnlyField(source='post.title')
    
    class Meta:
        model = Comment
        fields = ['created_at', 'updated_at', 'title',
                  'content', 'post', 'author']
