from django.urls import path
from . import views, blocked_users_views, like_views
"""
urls for Profile model.
"""


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('profile/<uuid:profile_id>/', views.profile_settings),
    path('profile/delete/<uuid:profile_id>/', views.delete_profile),
    path(
        'profile/blocked_list/<uuid:profile_id>/',
        blocked_users_views.get_blocked_users
    ),
    path(
        'profile/blocked_list/update/<uuid:profile_id>/',
        blocked_users_views.put_or_delete_blocked_users
    ),
    path('profile/like_list/update/<uuid:profile_id>/', like_views.update_list),
    path('profile/like_list/<uuid:profile_id>/', like_views.get_list),
    path('profile/random_feed/<uuid:profile_id>/', views.get_random_feed),
    path('profile/feed/<uuid:profile_id>/', views.get_feed),
]
