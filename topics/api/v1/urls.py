"""
API V1: Topics Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers
from .views import TopicViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topics_page')


###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
