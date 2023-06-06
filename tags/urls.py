"""
urls for Tags managment
"""
from django.urls import path
from . import views
"""
ROUTS
-----
'api/tags/': METHODS = 'GET'
    List all Tags
"""


urlpatterns = [
    path('tags/', views.tag_list),
]
