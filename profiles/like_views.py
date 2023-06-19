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
    """
    data = request.data
    aux = LikeUsers.objects.get(
        owner=Profile.objects.get(id=data.get('like_id'))
    )
    profile = Profile.objects.get(id=profile_id)

    if profile in aux.like_list:
        chat = Chat(
            user_one=profile,
            oser_two=Profile.objects.get(id=data.get('like_id'))
        )

        LikeUsers.objects.get(owner=profile).like_list.add(
            Profile.objects.get(id=data.get('like_id'))
        )

        return Response(
            {"it's a match!": f"Profiles {profile} and {date.get('like_id')} have a chat"},
            status=status.HTTP_201_CREATED
        )

    else:
        LikeUsers.objects.get(owner=profile).like_list.add(
            Profile.objects.get(id=data.get('like_id'))
        )
        return Response(
            {"done": f"{like_id} was added to {profile.id} like_list"},
            status=status.HTTP_202_ACCEPTED

        )

@api_view(['GET'])
def get_list(request, profile_id):
    """
    Get LikeUsers list o
    """
