from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from accounts.views import AccountViewSet


user_registration = AccountViewSet.as_view(actions={'post': 'register'})

router = DefaultRouter()
router.register('user-registration', user_registration)


urlpatterns = [
    url(r'^$', user_registration),
]
