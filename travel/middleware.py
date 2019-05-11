from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import re

EXCLUDE_URL = [
  '/api/user',
  '/api/travel',
  '/favicon.ico'
]

exclued_path = [re.compile(item) for item in EXCLUDE_URL]

class UserAuthMiddleware(MiddlewareMixin):
  def process_request(self, request):
    url_path = request.path
    for each in exclued_path:
      if re.match(each, url_path):
        return None
    return HttpResponseForbidden()