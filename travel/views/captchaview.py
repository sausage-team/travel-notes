"""
Captcha
"""
from logging import getLogger
from io import BytesIO
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import UserSerializer
from travel.models import User
from core.decorators.authorization import Authorization
from travel.util.captcha import create_validate_code
logger = getLogger(__name__)

class CaptchView(APIView):
    def get(self, request):
        f = BytesIO()
        img, code = create_validate_code()
        img.save(f,'PNG')
        request.session['code'] = code
        return HttpResponse(f.getvalue(), content_type="image/png")
        