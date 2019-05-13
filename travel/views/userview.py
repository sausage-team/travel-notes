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
from core.decorators.authorization import Authorization
logger = getLogger(__name__)

class UserBase(object):
    def get_user_by_id(self, id):
        """
        Find User By id
        """
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
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

class UserView(UserBase, APIView):
    @Authorization
    def get(self, request, uid):
        """
        Request user by uid
        """
        user = self.get_user(uid)
        serializer = UserSerializer(user)
        return Response(Wrapper(data=serializer.data))

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
        if self.get_user_by_np(data['username'],data['password']):
            return FAIL

        serializer = UserSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response(Wrapper(data=serializer.data))
        else:
            logger.info(serializer.errors)
        return FAIL

class UserCaptcha(UserView):
    """
    Captcha
    """
    pass

class UserForgetPwd(UserView):
    """
    Forget Password
    """
    def put(self, request):
        uid = request.session.get('uid', None)
        if uid is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        user = self.get_user_by_id(uid)
        data = request.data['data']

        if user.id_card == data['id_card']:
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
            return SUCCESS
        return FAIL

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