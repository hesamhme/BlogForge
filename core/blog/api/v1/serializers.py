from rest_framework import serializers
from ...models import Post, Category

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'author','title','content', 'snippet', 'status', 'category', 'created_date', 'publish_date']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']