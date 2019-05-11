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

    def get(self, request):
        """
        Request user by uid
        """
        user = self.get_user(request.query_params['uid'])
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response({'status':0, 'data':serializer.data})

    def put(self, request):
        """
        Update User By uid
        """
        user = self.get_user(request.query_params['uid'])
        if (user is None):
            return Response({'status': -1})

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0}, status=status.HTTP_200_OK)
        return Response({'status': -1})

    def post(self, request):
        """
        Create User
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':0, "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            logger.info(serializer.errors)
        return Response({'status':-1})
    def delete(self, request):
        """
        Delete User (Don't Allow)
        """
        return Response(status=status.HTTP_403_FORBIDDEN)