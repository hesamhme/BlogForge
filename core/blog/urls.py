from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post_list' ),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail' ),
    path('create/', views.PostCreateViews.as_view(), name = "create_view")
] 