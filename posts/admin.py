"""
Posts admin
"""
###
# Libraries
###
from django.contrib import admin
from .models import Post


###
# Inline Admin Models
###


###
# Main Admin Models
###
admin.site.register(Post)