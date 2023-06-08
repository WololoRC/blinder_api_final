from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from tags.models import Tags
from .serializers import ProfileSerializer
from datetime import datetime
import uuid
"""Views for authentication a Profile managment."""


@api_view(['POST'])
def signup(request):
    """
    Signup.

    METHODS: POST
    --------
        Create an authenticated User with Profile
        and retrive his Profile data.

        A .json body with fields 'username', 'password'
        and 'birth_date' is required.
    """
    try:
        data = request.data
        user = User.objects.create_user(
            username = data.get('username'),
            password = data.get('password')
        )

        user.save()
        token = Token.objects.create(user=user)

        profile = Profile(
            user = user,
            description = "",
            birth_date = datetime.strptime(data.get('birth_date'), "%Y-%m-%d")
        )

        profile.save()

        return Response(
            {
                'token': str(token),
                'username': str(user.username),
                'id': profile.id,
            },
            status=status.HTTP_201_CREATED
        )

    except IntegrityError:
        return Response(
            {'error': 'username taken. chose another'},
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

    profile = Profile.objects.get(user=user)

    token = Token.objects.get(user=user)
    return Response(
            {'token': str(token), 'username': user.username, "id": profile.id}
    )

@api_view(['GET','PUT'])
def profile_settings(request, profile_id):
    """
    Profile settings.

    An a Autorization header with Token <user-token>
    is required. (TODO)

    METHODS: 'PUT', 'GET'.
    -------
    ...........................................................
    PUT:
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
    ...........................................................
    GET:
        Get user Profile on success, else a error message.
    ...........................................................

    """

    if request.method == 'PUT':
        data = request.data
        profile = Profile.objects.get(id=profile_id)
        serializer = ProfileSerializer(profile)

        # if there are some tags to remove.
        if 'remove_tags' in data:
            tags = Tags.objects.filter(id__in=data.get('remove_tags', []))
            profile.owner_tags.remove(*tags)

        # if we want add some tags.
        elif 'add_tags' in data:
            tags = Tags.objects.filter(id__in=data.get('add_tags', []))
            profile.owner_tags.add(*tags)

        # change description
        elif 'description' in data:
            profile.description = data.get('description')

        else:
            return Response(
                {'error': "no field provided on request, 'remove_tags', 'add_tags' or 'description'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        profile.save()
        return Response(serializer.data)

    if request.method == 'GET':
        try:
            profile = Profile.objects.get(id=profile_id)
            serializer = ProfileSerializer(profile)

            return Response(serializer.data)

        except Profile.DoesNotExist:
            return Response(
                {'error': 'User does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['DELETE'])
def delete_profile(request, profile_id):
    """
    An a Autorization header with Token <user-token>
    is required. (TODO)

    Deletes a user Profile.

    On success return a http 204 status or a error message
    if fails.

    """
    try:
        profile = Profile.objects.get(id=profile_id)
        User.objects.get(pk=profile.user.pk).delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    except Profile.DoesNotExist:
        return Response(
            {'error': 'User does not exist'},
            status=status.HTTP_400_BAD_REQUEST
        )

