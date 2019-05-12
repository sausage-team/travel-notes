from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from functools import update_wrapper, partial

class Authorization(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        request = args[1]
        if isinstance(request, Request):
            uid = request.session.get('uid', None)
            print(uid)
            if uid:
                return self._func(*args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def __get__(self, instance, owner):
        return partial(self.__call__, instance)
