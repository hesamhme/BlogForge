from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    # path('post/', views.post_list ) ==> this is for FBV,
    path('post/', views.PostList.as_view(), name='postlist' ),
    path('post/<int:id>/', views.post_detail ),
] 