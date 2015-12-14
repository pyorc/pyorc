import os

from django.views.generic import View
from django.http.response import HttpResponse
from pbkdf2 import PBKDF2

from accounts.models import UserDAO
from utils.helper import parse_request


class AuthenticationView(View):

    @parse_request
    def post(self, request):
        salt = os.urandom(16).encode('hex')
        username = request.dict_data['username']
        password = request.dict_data['password']
        password_hash = PBKDF2(password, salt).hexread(16)
        UserDAO.add_user(username, password_hash, salt)
        return HttpResponse(status=201)
