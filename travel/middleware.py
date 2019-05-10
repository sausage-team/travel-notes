from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import re

EXCLUDE_URL = [
  '/register',
  '/login',
  '/travel',
  '/api',
  '/favicon.ico'
]
INCLUDE_URL = []

exclued_path = [re.compile(item) for item in EXCLUDE_URL]
include_path = [re.compile(item) for item in INCLUDE_URL]

class UserAuthMiddleware(MiddlewareMixin):
  def process_request(self, request):
    url_path = request.path
    for each in exclued_path:
      if re.match(each, url_path):
        return None
    return HttpResponseForbidden()