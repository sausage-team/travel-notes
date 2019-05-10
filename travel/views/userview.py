from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from travel.serializers import UserSerializer
from travel.models import User

class UserView(APIView):
  def get(self, request):
    print('Get Called')
    user = User.objects.all()
    serializer  = UserSerializer(user, many = True)
    return Response(serializer.data)
  def post(self, request):
    print('Post Called')
    return Response(status = status.HTTP_404_NOT_FOUND)
  def put(self, request):
    print('Put Called')
    return Response(status = status.HTTP_404_NOT_FOUND)
  def delete(self, request):
    print('Delete Called')
    return Response(status = status.HTTP_404_NOT_FOUND)