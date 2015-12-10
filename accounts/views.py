from django.views.generic import View
from django.http.response import HttpResponse


class AuthenticationView(View):

    def post(self, request):
        return HttpResponse()
