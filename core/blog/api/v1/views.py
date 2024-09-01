from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from blog.models import Post

# first api base function
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data)
    elif request.method == "POST":
        posts_serializer = PostSerializer(data = request.data)
        posts_serializer.is_valid(raise_exception=True)
        posts_serializer.save()
        return Response(posts_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)
    elif request.method == "PUT":
        post_serializer = PostSerializer(post, data=request.data)
        post_serializer.is_valid(raise_exception=True)
        post_serializer.save()
        return Response(post_serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)






