from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed
from django.urls import path

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('feed/', user_feed, name='user-feed'),
]

urlpatterns += router.urls
