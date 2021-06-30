"""
Topics admin
"""
###
# Libraries
###
from django.contrib import admin
from .models import Topic

###
# Inline Admin Models
###


###
# Main Admin Models
###
admin.site.register(Topic)