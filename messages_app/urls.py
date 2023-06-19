from django.urls import path
from . import views
"""urls for messages_app"""


urlpatterns = [
    path('chat/<uuid:chat_id>/', views.get_delete_chat),
    path('chat/messages/<uuid:chat_id>/', views.put_chat),
    path('chat/inbox/<uuid:profile_id>/', views.get_from_user)
]
