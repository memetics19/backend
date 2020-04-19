import json
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase

from login_api.serializers import UserProfileSerializer
from login_api.models import UserProfileManager, UserProfileManager


class LoginTestCase(APITestCase):

    def test_login(self):
        data = {"email": "test@memetics.in",
                "name": "testcase",
                "password": "testing@123"}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileUpdateTestCae(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testing@memetics.in",
                                             password="testing@123")
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token)
