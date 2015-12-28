from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from accounts.token import token_required


class PostViewSet(ViewSet):

    def retrieve(self, request, post_id):
        pass

    def list(self, request):
        pass

    @token_required
    def create(self, request):
        pass
        return Response()

    def delete(self, request, post_id):
        pass
