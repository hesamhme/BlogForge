from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    # path('post/', views.post_list ) ==> this is for FBV,
    # path('post/<int:id>/', views.post_detail )  ==> this is for FBV,
    path('post/', views.PostList.as_view(), name='post_list' ),
    path('post/<int:id>', views.PostDetail.as_view(), name='post_detail' ),
    
] 