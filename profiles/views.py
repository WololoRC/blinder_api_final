from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Profile, BlockedUsers, LikeUsers
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

        Also set a BlockedUsers table for user.

        A .json body with fields 'username', 'password'
        and 'birth_date' is required.

        Returns:
            User credential on success, a ugly error message if fails.
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

        blocked_users = BlockedUsers(owner=profile)
        like_users = LikeUsers(owner=profile)

        blocked_users.save()
        like_users.save()

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

    except TypeError:
        user.delete()
        return Response(
            {"error": "put a correct 'birth_date' with content '%Y-%d-%m' you stupid."},
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
            {'token': str(token), 'username': user.username, "id": profile.id},
            status.HTTP_200_OK
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
        try:
            data = request.data
            profile = Profile.objects.get(id=profile_id)
            serializer = ProfileSerializer(profile)

        except (Profile.DoesNotExist, ValidationError):
            return Response(
                {'error': 'User does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # if there are some tags to remove.
        if 'remove_tags' in data and 'description' in data:
            tags = Tags.objects.filter(id__in=data.get('remove_tags', []))
            profile.owner_tags.remove(*tags)
            profile.description = data.get('description')
        # if we want add some tags.
        elif 'add_tags' in data and 'description' in data:
            tags = Tags.objects.filter(id__in=data.get('add_tags', []))
            profile.owner_tags.add(*tags)
            profile.description = data.get('description')
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

        except (Profile.DoesNotExist, ValidationError):
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

    except (Profile.DoesNotExist, ValidationError):
        return Response(
            {'error': 'User does not exist'},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def get_random_feed(request, profile_id):
    """
    Get feed!!

    Get a Profile list for populate the feed.

    Returns:
    On success all Profile excluding the Profiles inside of
    LikeUsers and BlockedUsers, else a error message.
    """
    try:
        profile = Profile.objects.get(id=profile_id)
        like = LikeUsers.objects.get(owner=profile)
        block = BlockedUsers.objects.get(owner=profile)

        this_ids = [item.id for item in like.like_list.all()]
        this_ids.extend([item.id for item in block.blocked_list.all()])
        this_ids.extend([profile.id])

    except (Profile.DoesNotExist, ValidationError):
        return Response({'error': '{profile_id} is not valid, dont be stupid.'})

    feed = Profile.objects.exclude(id__in=this_ids)

    return Response(ProfileSerializer(feed, many=True).data)

@api_view(['GET'])
def get_feed(request, profile_id):
    """
    Get feed!!

    Get a Profile list for populate the feed.

    Returns:
    On success all Profile by exception of block and likes,
    thath match almost once with the 'owner_tags' of the main user.
    Else a error message.
    """
    try:
        profile = Profile.objects.get(id=profile_id)
        like = LikeUsers.objects.get(owner=profile)
        block = BlockedUsers.objects.get(owner=profile)

        this_ids = [item.id for item in like.like_list.all()]
        this_ids.extend([item.id for item in block.blocked_list.all()])
        this_ids.extend([profile.id])

    except (Profile.DoesNotExist, ValidationError):
        return Response({'error': '{profile_id} is not valid, dont be stupid.'})

    p_tags = list(profile.owner_tags.all())
    feed = Profile.objects.exclude(id__in=this_ids)
    last_profiles = []

    for item in feed.all():
        for tag in item.owner_tags.all():
            if tag in p_tags:
                last_profiles.append(item)

    last_profiles = [item.id for item in last_profiles]
    feed = Profile.objects.filter(id__in=last_profiles)

    return Response(ProfileSerializer(feed, many=True).data)
