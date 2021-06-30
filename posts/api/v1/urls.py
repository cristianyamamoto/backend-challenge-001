"""
API V1: Posts Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers
from topics.api.v1.urls import router as topic_router
from .views import PostViewSet


###
# Routers
###
""" Main router """
router = routers.NestedSimpleRouter(topic_router, r'topics', lookup='topic')
router.register(r'posts', PostViewSet, basename='posts_page')

###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
