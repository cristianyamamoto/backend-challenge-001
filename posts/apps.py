"""
Posts Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class PostsConfig(AppConfig):
    name = 'posts'

    def ready(self):
        import posts.signals
