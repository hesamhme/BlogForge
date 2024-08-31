from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from blog.models import Post

# first api base function
@api_view()
def post_list(request):
    posts = Post.objects.filter(status=True)
    posts_serializer = PostSerializer(posts, many=True)
    return Response(posts_serializer.data)

@api_view()
def post_detail(request, id):

    post = get_object_or_404(Post, pk=id, status=True)
    post_serializer = PostSerializer(post)
    return Response(post_serializer.data)







