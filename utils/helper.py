#!/usr/bin/env python
# coding=utf-8

import uuid

from rest_framework.settings import api_settings


def uuid_key():
    return uuid.uuid4().hex


def get_paginated_response(request, queryset, serializer_class):
    paginator = api_settings.DEFAULT_PAGINATION_CLASS()
    page = paginator.paginate_queryset(queryset, request)
    data = serializer_class(page, many=True).data
    return paginator.get_paginated_response(data)
