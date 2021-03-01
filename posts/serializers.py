from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from posts.models import Post
from topics.models import Topic


class CreatePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'created_at', 'updated_at', 'title',
                 'content']

class RetrievePostSerializer(serializers.ModelSerializer):
    
    author = UserDetailsSerializer(read_only=True)
    topic = serializers.ReadOnlyField(source='topic.url_name')
    
    class Meta:
        model = Post
        fields = ['id', 'created_at', 'updated_at', 'title',
                 'content', 'topic', 'author']