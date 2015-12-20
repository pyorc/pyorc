from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet


router = DefaultRouter()
router.register('post_view', PostViewSet)


PostViewSet.as_view(actions={'get': 'retrieve', 'delete': 'destroy'})
PostViewSet.as_view(actions={'post': 'create', 'get': 'list'})


urlpatterns = [
    # url(),
]
