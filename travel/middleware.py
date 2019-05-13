from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import re

EXCLUDE_URL = [
    r'^\/api\/user(\/[0-9a-zA-Z-]+)?$',
    r'^\/api\/article(\/.*)?$',
    r'^\/captcha(\/.*)?$',
    r'/favicon.ico'
]

exclued_path = [re.compile(item) for item in EXCLUDE_URL]

class UserAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        url_path = request.path
        for each in exclued_path:
            if re.match(each, url_path):
                return None
        uid = request.session.get('uid', None)
        # TODO
        # retrive user
        if uid:
            return None
        return HttpResponseForbidden()