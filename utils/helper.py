#!/usr/bin/env python
# coding=utf-8

import json
import uuid


def parse_request(func):
    def wrapper(_, request, *args, **kw):
        if request.method == 'GET':
            request.dict_data = dict(request.GET)
        else:
            request.dict_data = json.loads(request.body)
        return func(_, request, *args, **kw)
    return wrapper


def uuid_key():
    return uuid.uuid4().hex
