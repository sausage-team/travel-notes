"""
User Operation
"""
from logging import getLogger
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import UserSerializer
from travel.models import User
from travel.bean.wrapper import Wrapper, SUCCESS, FAIL
logger = getLogger(__name__)

class UserView(APIView):
    def get_user(self, uid):
        """
        Find User by uid
        """
        try:
            return User.objects.get(uid=uid)
        except User.DoesNotExist:
            return None
    def get_user_by_np(self, username, pwd):
        """
        Find User by username and password
        """
        try:
            return User.objects.get(username=username, password=pwd)
        except User.DoesNotExist as exp:
            logger.error(exp)
            return None

    def get(self, request, uid):
        """
        Request user by uid
        """
        user = self.get_user(uid)
        serializer = UserSerializer(user)
        return Response(Wrapper(data=serializer.data))

    def put(self, request, uid):
        """
        Update User By uid
        """
        user = self.get_user(uid)
        if (user is None):
            return FAIL

        serializer = UserSerializer(user, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return SUCCESS
        return FAIL

    def post(self, request):
        """
        Create User
        """
        serializer = UserSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response(Wrapper(data=serializer.data))
        else:
            logger.info(serializer.errors)
        return FAIL
    def delete(self, request):
        """
        Delete User (Don't Allow)
        """
        return Response(status=status.HTTP_403_FORBIDDEN)

class UserRegister(UserView):
    def post(self, request):
        return super().post(request)

class UserLogin(UserView):
    """
    User Login
    """
    def post(self, request):
        data = request.data['data']
        user = self.get_user_by_np(data["username"], data["password"])
        if user is None:
            logger.error('user does exsit')
            return FAIL
        uid = request.session.get('uid', default=None)
        if uid is None or uid == '':
            request.session['uid'] = user.uid
            return SUCCESS
        return FAIL

class UserLogout(UserView):
    """
    User Logout
    """
    def get(self, request):
        uid = request.session.get('uid', default=None)
        logger.error(uid)
        if uid:
            request.session['uid'] = ''
            return SUCCESS
        return FAIL