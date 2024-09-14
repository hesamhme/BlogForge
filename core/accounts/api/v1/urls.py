from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registrations/', views.RegistrationsApiView.as_view(), name='registrations'),
    
    path('email/test', views.TestEmailSend.as_view(), name='test-mail'),
    # activation
    path('activation/confirm/<str:token>', views.ActivationApiView.as_view(), name = 'activation' ),

    # activationresend
    # path('activation/resend', ),
    
    # resend activation
    # path('resend-activations/'),
    # change password
    path('change-password/', views.ChangePasswordViews.as_view(), name='change-password'),
    
    # reset password
    
    # login token
    path('token/login/', views.CustomObtainAuthToken.as_view() , name='token-login'),
    
    # logout token
    path('token/logout/', views.CustomDiscardAuthToken.as_view() , name='token-logout'),
    
    # login jwt
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),

    # profile
    path('profile/', views.ProfileApiView.as_view(), name='jwt_verify'),
] 
