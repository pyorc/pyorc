from django.conf.urls import url

from accounts.views import AccountViewSet


user_registration = AccountViewSet.as_view(actions={'post': 'register'})
user_authentication = AccountViewSet.as_view(actions={'post': 'login'})

urlpatterns = [
    url(r'^$', user_registration),
    url(r'^authentication$', user_authentication),
]
