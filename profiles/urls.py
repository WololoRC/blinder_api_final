from django.urls import path
from . import views, blocked_users_views
"""
urls for Profile model.
-----------------------
ROUTS:
..........................................................
'api/signup/': METHODS: 'POST'.

    Create an authenticated User and retrive his Profile data.

    A .json body with fields 'username', 'password'
    and 'birth_date' is required.
    ..........................................................
'api/login/': METHODS: 'POST'.

    Get User credentials and return a authenticatio token
    if User is authenticated.

    A .json body with fields 'username' and 'password
    is required'.
..........................................................
'profile/<uuid:profile_id>/': METHODS: 'GET', 'PUT'.

PUT:
---
    Update Profile tags and description, send a .json body
    with fields:
    - 'remove_tags': <Tag's UUID's'>
        delete tags.

    - 'add_tags': <Tag's UUID's>.
        add tags.

    - 'description': str.
        change description.

    On success returns a updated Profile instance,
    else an error message.

GET:
---
    Get user Profile on success, else a error message.
..........................................................
'profile/delete/<uuid:profile_id>/': METHODS: 'DELETE'.

    An a Autorization header with Token <user-token>
    is required.

    Deletes a user Profile.

    On success return a http 204 status or a error message
    if fails.


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
    )
]
