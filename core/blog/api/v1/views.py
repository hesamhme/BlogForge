from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .serializers import PostSerializer
from blog.models import Post


class PostList(APIView):

    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # getting a list of post and create new posts

    def get(self, request):
        # retriveing a list of posts
        posts = Post.objects.filter(status=True)
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data)
    
    def post(self, request):
        # creating a post with provided data
        posts_serializer = PostSerializer(data = request.data)
        posts_serializer.is_valid(raise_exception=True)
        posts_serializer.save()
        return Response(posts_serializer.data)


class PostDetail(APIView):
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post_serializer = self.serializer_class(post)
        return Response(post_serializer.data)
    
    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post_serializer = PostSerializer(post, data=request.data)
        post_serializer.is_valid(raise_exception=True)
        post_serializer.save()
        return Response(post_serializer.data)
    
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)



'''
the function base view is old structure, i used here to just show my ability 
knowing how to using them

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


'''