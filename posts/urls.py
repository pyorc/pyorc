from django.conf.urls import url

from posts.views import PostViewSet


post_detail = PostViewSet.as_view(actions={'get': 'retrieve', 'delete': 'destroy'})
post_list = PostViewSet.as_view(actions={'post': 'create', 'get': 'list'})


urlpatterns = [
    url('^$', post_list),
    url('^/(?P<post_id>\w+)', post_detail)
]
