"""
User Operation
"""
from logging import getLogger
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.bean.wrapper import Wrapper, SUCCESS, FAIL
from core.decorators.authorization import Authorization
from travel.serializers import UserSerializer
from travel.models import User
from travel.bean.userwrapper import UserWrapper
from travel.bean.articlewrapper import ArticleWrapper
logger = getLogger(__name__)

class UserBase(object):
    def get_user(self, uid):
        """
        Find User by uid
        """
        try:
            return User.objects.get(id=uid)
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
    def get_user_by_name(self, username):
        """
        Find User by username
        """
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist as exp:
            logger.error(exp)
            return None

class UserView(UserBase, APIView):
    @Authorization
    def get(self, request, uid):
        """
        Request user by uid
        """
        user = self.get_user(uid)
        serializer = UserSerializer(user)
        return Response(UserWrapper(data=serializer.data))

    @Authorization
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

    @Authorization
    def delete(self, request, uid):
        """
        Delete User (Don't Allow)
        """
        return Response(status=status.HTTP_403_FORBIDDEN)

class UserRegister(UserView):
    """
    User Register
    """
    def post(self, request):
        """
        Create User
        """
        data = request.data['data']
        if self.get_user_by_name(data['username']):
            return FAIL

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(UserWrapper(data=serializer.data))
        else:
            logger.info(serializer.errors)
        return FAIL

class UserForgetPwd(UserView):
    """
    Forget Password
    """
    def put(self, request):
        uid = request.session.get('uid', None)
        if uid is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        user = self.get_user(uid)
        data = request.data['data']

        if user.phone == data['phone']:
            user.password = data['password']
            user.save()
            return SUCCESS
        return FAIL

class UserLogin(UserView):
    """
    User Login
    """
    def post(self, request):
        data = request.data['data']
        user = self.get_user_by_np(data["username"], data["password"])
        if user is None:
            logger.error('user does exsit')
            return Response(status=status.HTTP_403_FORBIDDEN)
        uid = request.session.get('uid', default=None)
        if uid is None:
            request.session['uid'] = user.id
        serializer = UserSerializer(user)
        return Response(UserWrapper(data=serializer.data))

class UserLogout(UserView):
    """
    User Logout
    """
    @Authorization
    def get(self, request):
        uid = request.session.get('uid', default=None)
        if uid:
            request.session['uid'] = None
            request.session.clear()
            return SUCCESS
        return FAIL