from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'author','title','content', 'image', 'snippet', 'status', 'category', 'created_date', 'publish_date']
        read_only_fields = ['author']

    # to seprate and rganize serializer for list and detail view
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
        else:
            rep.pop('content', None)

        rep['category'] = CategorySerializer(instance.category).data  
        return rep
    
    def create(self, validated_data):
        # specific author 
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']