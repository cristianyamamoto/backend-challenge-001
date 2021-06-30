"""
API V1: Comments Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers
from posts.api.v1.urls import router as post_router
from .views import CommentViewSet

###
# Routers
###
""" Main router """
router = routers.NestedSimpleRouter(post_router, r'posts', lookup='post')
router.register(r'comments', CommentViewSet, basename='comments_page')

###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
