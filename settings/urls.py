"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin

from helpers.health_check_view import health_check

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from topics.views import TopicViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet

topic_router = DefaultRouter()
topic_router.register(r'topics', TopicViewSet, basename='topics_page')

post_router = NestedSimpleRouter(topic_router, r'topics', lookup='topic')
post_router.register(r'posts', PostViewSet, basename='posts_page')

comment_router = NestedSimpleRouter(post_router, r'posts', lookup='post')
comment_router.register(r'comments', CommentViewSet, basename='comments_page')

###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include(topic_router.urls)),
    url(r'^', include(post_router.urls)),
    url(r'^', include(comment_router.urls)),
]
