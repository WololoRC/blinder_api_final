from django.urls import path
from . import views
"""
urls for Profile model.
-----------------------
ROUTS:
..........................................................
'api/signup/': METHODS: 'POST'.

    Create a user and retrive a token authentication.

    A .json body with fields 'username'
    and 'password' is required.
..........................................................
'api/login/': METHODS: 'POST'.

    Get User credentials and return a authenticatio token
    if User is authenticated.

    A .json body with fields 'username' and 'password
    is required'.
..........................................................
'api/profile/': METHODS: 'POST'.

    An Authorization header with user's token is required.
    e.g: 'Authorization: Token <token>'.

    POST:
        Create a Profile for User.

        A .json body with fields: 'user_id', 'description' and 'birth_age'
        is required.

        birth_age must have this format '1997-2-4'.
"""


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('profile/', views.profile_settings)
]
