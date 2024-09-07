from rest_framework import serializers

from ...models import User


class RegistrationsSerializerClass(serializers.ModelSerializer):
    password1 = serializers.CharField(max_lengh=255, write_only = True)
    class Meta:
        model = User
        fields = ['email', 'password', 'password1']

        def validate(self, attrs):
            if attrs.get('password') != attrs.get('password1'):
                raise serializers.ValidationError({'detail': 'passwords dosenot match'})

            return super().validate(attrs)