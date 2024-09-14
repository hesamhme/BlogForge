from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.conf import settings

from mail_templated import EmailMessage

from .serializers import (
    RegistrationsSerializerClass, 
    CustomAuthTokenSerializer, 
    ChangePasswordSerializer, 
    ProfileSerializer
) 
from ...models import User, Profile
from ..utils import EmailThreading


class RegistrationsApiView(generics.GenericAPIView):
    serializer_class = RegistrationsSerializerClass

    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializerClass(data = request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'message': 'user created successfully',
                'detail': f" you registered with email: {email} ",
            }
            
            user_obj = get_object_or_404(User, email = email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl', {'token': token}, 'admin@admin.com', to=[email])
            EmailThreading(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)



class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    

class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ChangePasswordViews(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated,]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['wrong password']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            data = {'detail': 'password changed successfuly'}
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class ActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        # decode token
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response({'detail': 'token expired'}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'detail': 'token is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        # create user obj and active account
        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verifeid:
            return Response({'details': 'your account is already verified'})
        user_obj.is_verifeid= True
        user_obj.save()

        return Response({'details': 'your account has been successful verified'})



class ActivationResendApiView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            user_obj = get_object_or_404(User, email = email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/hello.tpl', {'token': token}, 'admin@admin.com', to=[email])
            EmailThreading(email_obj).start()
            return Response({'detail': 'user activation resend successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)





class TestEmailSend(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        self.email = 'user@user.com'
        user_obj = get_object_or_404(User, email = self.email)
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/hello.tpl', {'token': token}, 'admin@admin.com', to=[self.email])
        EmailThreading(email_obj).start()
        return Response('sent!!!!')
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
