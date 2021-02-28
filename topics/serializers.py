from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
# from posts.models import Post
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):

    author = UserDetailsSerializer(read_only=True)
    # posts = PostSerializer(read_only=True, many=True)
    
    class Meta:
        model = Topic
        fields = ['created_at', 'updated_at', 'title',
                  'name', 'description', 'url_name', 'author']
        # fields = ['created_at', 'updated_at', 'title',
        #           'name', 'description', 'url_name', 'author', 'posts']

# class CreateTopicSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Topic
#         fields = ['created_at', 'updated_at', 'title',
#                  'name', 'description', 'url_name', 'author']


# class RetrieveTopicSerializer(serializers.ModelSerializer):

#     author = UserDetailsSerializer(read_only=True)
#     posts = PostSerializer(read_only=True, many=True)
    
#     class Meta:
#         model = Topic
#         fields = ['created_at', 'updated_at', 'title',
#                   'name', 'description', 'url_name', 'author', 'posts']
