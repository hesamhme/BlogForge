from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post_list' ),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail' ),
    path('create/', views.PostCreateViews.as_view(), name = "create_view"),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name = 'edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'delete'),
    path('api/v1/', include('blog.api.v1.urls')),
] 