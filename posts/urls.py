from django.conf.urls import url

from posts.views import PostViewSet


PostViewSet.as_view(actions={'get': 'retrieve', 'delete': 'destroy'})
PostViewSet.as_view(actions={'post': 'create', 'get': 'list'})


urlpatterns = [
    # url(),
]
