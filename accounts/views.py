from django.views.generic import View
from django.http.response import HttpResponse


class LoginView(View):

    def get(self, request):
        print 'foo'
        return HttpResponse()
