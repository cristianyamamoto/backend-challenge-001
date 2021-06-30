"""
Comments admin
"""
###
# Libraries
###
from django.contrib import admin
from .models import Comment


###
# Inline Admin Models
###


###
# Main Admin Models
###
admin.site.register(Comment)