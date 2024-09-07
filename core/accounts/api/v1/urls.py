from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registrations/', views.RegistrationsApiView.as_view(), name='registrations')
    # change password
    # reset password
    # login token
    # login jwt
] 