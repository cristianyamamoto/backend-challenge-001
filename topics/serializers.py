from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from topics.models import Topic


class CreateTopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ['id', 'created_at', 'updated_at', 'title',
                  'name', 'description', 'url_name']

class RetrieveTopicSerializer(serializers.ModelSerializer):
    
    author = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'created_at', 'updated_at', 'title',
                  'name', 'description', 'url_name', 'author']
