from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from datetime import datetime
"""Views for authentication a Profile managment."""


@api_view(['POST'])
def signup(request):
    """
    Signup.

    METHODS:
    --------
        Create a user and retrive a token authentication.

        A .json body with fields 'username'
        and 'password' is required.
    """
    try:
        data = request.data
        user = User.objects.create_user(
            username = data.get('username'),
            password = data.get('password')
        )

        user.save()

        token = Token.objects.create(user=user)
        return Response(
            {
                'token': str(token),
                'username': str(user.username),
                'id': user.pk
            },
            status=status.HTTP_201_CREATED
        )

    except IntegrityError:
        return Response(
            {'error': 'username taken. choose another'},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def login(request):
    """
    Login.

    METHODS: 'POST'
        Get User credentials and return a authenticatio token
        if User is authenticated.

        A .json body with fields 'username' and 'password
        is required'.
    """
    data = request.data
    user = authenticate(
        request,
        username=data.get('username'),
        password=data.get('password')
    )

    if user is None:
        return Response(
            {'error': 'user does not exist'},
            status=status.HTTP_400_BAD_REQUEST
        )

    token = Token.objects.get(user=user)
    return Response(
            {'token': str(token), 'username': user.username, "id": user.pk}
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile_settings(request):
    """
    An Authorization header with user's token is required.
    e.g: 'Authorization: Token <token>'.

    METHODS: 'POST'

    POST:
        Create a Profile for User.

        A .json body with fields: 'user_id', 'description' and 'birth_age'
        is required.

        birth_age must have this format '1997-2-4'
    """
    if request.method == 'POST':
        data = request.data
        user = User.objects.get(pk=data.get('user_id'))
        birth_date = datetime.strptime(data.get('birth_age'), "%Y-%m-%d")

        profile = Profile(
            user = user,
            description = data.get('description'),
            birth_age = birth_date
        )

        return Response(ProfileSerializer(profile).data)

