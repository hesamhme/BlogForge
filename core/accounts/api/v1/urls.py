from django.urls import path, include
# from rest_framework.authtoken.views import ObtainAuthToken
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registrations/', views.RegistrationsApiView.as_view(), name='registrations'),
    
    # change password
    # reset password
    
    # login token
    path('token/login/', views.CustomObtainAuthToken.as_view() , name='token-login'),
    
    # logout token
    path('token/logout/', views.CustomDiscardAuthToken.as_view() , name='token-logout'),
    
    # login jwt
] 
