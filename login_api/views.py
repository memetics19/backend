from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from login_api import models
from login_api import serializers

# Create your views here.

class UserLoginAPIView(ObtainAuthToken):
    """Handling creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileViewSet(viewsets.ModelViewSet):
    """"Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    
