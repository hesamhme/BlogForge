from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "api-v1"

router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls



# urlpatterns = [
#     # path('post/', views.post_list ) ==> this is for FBV,
#     # path('post/<int:id>/', views.post_detail )  ==> this is for FBV,
#     # path('post/', views.PostList.as_view(), name='post_list' ),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail' ),
#     path('post/', views.PostViewSet.as_view({'get':'list'}), name='post_list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrive'}), name='post_detail'), 
   
# ] 

