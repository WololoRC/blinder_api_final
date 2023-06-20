from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Profile, LikeUsers
from messages_app.models import Chat


@api_view(['PUT'])
def update_list(request, profile_id):
    """
    Add users profiles or make a match.

    A payload with keys 'like_id' with a valid
    profiles id is required.

    Returns:
    If like_list from liked Profile have record of the
    main User a Chat instance is created, else only saves
    the liked Profile on the like_list of main User.

    if profile_id or like_id are not valid returns a error
    message.
    """
    try:
        data = request.data
        aux = LikeUsers.objects.get(
            owner=Profile.objects.get(id=data.get('like_id'))
        )
        profile = Profile.objects.get(id=profile_id)

    except (Profile.DoesNotExist, ValidationError):
        return Response(
            {'error': "profile_id or like_id are not valid"},
            status=status.HTTP_404_NOT_FOUND
        )

    if profile in aux.like_list.all():
        chat = Chat(
            user_one=profile,
            user_two=Profile.objects.get(id=data.get('like_id'))
        )

        LikeUsers.objects.get(owner=profile).like_list.add(
            Profile.objects.get(id=data.get('like_id'))
        )
        chat.save()

        return Response(
            {"it's a match!": f"Profiles {profile.id} and {data.get('like_id')} have a chat"},
            status=status.HTTP_201_CREATED
        )

    else:
        LikeUsers.objects.get(owner=profile).like_list.add(
            Profile.objects.get(id=data.get('like_id'))
        )
        return Response(
            {"done": f"{data.get('like_id')} was added to {profile.id} like_list"},
            status=status.HTTP_202_ACCEPTED

        )

@api_view(['GET'])
def get_list(request, profile_id):
    """
    Get LikeUsers list from Profile

    On success returns Profile like_list, else
    return a ugly error message.
    """
    try:
        profile = Profile.objects.get(id=profile_id)
        likes = LikeUsers.objects.get(owner=profile)
        likes = [item.id for item in likes.like_list.all()]

        return Response(
            {'like_list': likes},
            status=status.HTTP_200_OK
        )

    except (Profile.DoesNotExist, ValidationError):
        return Response(
            {'error': 'profile_id is not valid'},
            status=status.HTTP_404_NOT_FOUND
        )
