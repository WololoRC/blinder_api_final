"""
Views for Tags managment
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tags
from .serializers import TagsSerializer


@api_view(['GET'])
def tag_list(request):
    """
    Get all tags

    METHODS:
    --------
    GET:
        List all tags
    """
    tag_list = Tags.objects.all()
    serializer = TagsSerializer(tag_list, many=True)

    return Response(serializer.data)
