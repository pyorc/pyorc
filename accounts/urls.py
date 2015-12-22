from django.conf.urls import url

from accounts.views import AccountViewSet
from rest_framework.authtoken import views


user_registration = AccountViewSet.as_view(actions={'post': 'register'})

urlpatterns = [
    url(r'^$', user_registration),
    url(r'^authentication$', views.obtain_auth_token),
]
