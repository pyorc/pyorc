from django.conf.urls import url

from accounts.views import AccountViewSet
from rest_framework.authtoken import views


user_registration = AccountViewSet.as_view(actions={'post': 'register'})
user_authentication = AccountViewSet.as_view(actions={'post': 'authentication'})

urlpatterns = [
    url(r'^$', user_registration),
    url(r'^/authentication$', user_authentication),
]
