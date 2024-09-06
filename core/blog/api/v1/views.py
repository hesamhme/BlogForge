from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404


from .serializers import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import LargeResultsSetPagination
from blog.models import Post, Category


# using model view sets
class PostModelViewSet(viewsets.ModelViewSet):
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # query set
    queryset = Post.objects.filter(status=True)

    # filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'category']
    search_fields = ['title', 'content']
    ordering_fields = ['publish_date']
    pagination_class = LargeResultsSetPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
 

'''
# using view sets
class PostViewSet(viewsets.ViewSet):
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # query set
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    '''


'''
class PostList(ListCreateAPIView):
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # query set
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    # getting detail of the post edit and delete it
    
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # query set
    queryset = Post.objects.filter(status=True)'''


'''
USING MIXINS 
class PostDetailGenericView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # getting detail of the post edit and delete it
    
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # query set
    queryset = Post.objects.filter(status=True)

    # looking for
    # lookup_field = 'id'

    def get(self, request,*args, **kwargs):
        # retrive data
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request,*args, **kwargs):
        # update data
        return self.update(request, *args, **kwargs)
    
    def delete(self, request,*args, **kwargs):
        # delete data
        return self.delete(request, *args, **kwargs)'''
    


'''
USING MIXINS POST LIST VIEW
class PostListGenericView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    # permissions classes
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #serializer class for easy data input
    serializer_class = PostSerializer

    # query set
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        
        # retriveing a list of posts
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''

'''
USING APIVIEW POST LIST VIEW
class PostListApiView(APIView):

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
        return Response(posts_serializer.data)'''


'''
USING APIVIEW POST DETAIL
class PostDetailApiView(APIView):
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

'''
USING FBV
the function base view is old structure, i used here to just show my ability 
knowing how to using them

# first api base function
@api_view(['GET', 'POST'])
def post_list_fbv(request):
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
def post_detail_fbv(request, id):
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