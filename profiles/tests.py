from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class AuthenticationTest(TestCase):
    """
    Tests on Authentication.
    """
    def setUp(self):
        self.client = APIClient()

    def test_signup(self):
        """
        Signup works as expected.
        """
        url = '/api/signup/'
        data = {
            'username' : 'wololo',
            'password' : 'pwd',
            'birth_date': '1990-4-5'
        }

        response1 = self.client.post(url, data)
        response2 = self.client.post(url, data)


        print(f"payload: {data}\n")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        print(f"signup: {response1.data}\n")
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        print(f"signup with same credentials: {response2.data}'\n'")

    def test_login(self):
        """
        Login works as expected
        """
        data = {
            'username' : 'wololo',
            'password' : 'pwd',
            'birth_date': '1990-4-5'
        }

        response1 = self.client.post('/api/signup/', data)

        data.pop('birth_date')

        response2 = self.client.post('/api/login/', data)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        print(f"login successful: {response2.data}\n")

        data.update({'password': 'pwd1'})
        response = self.client.post('/api/login/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print(f"login fails: {response.data}")

class ProfileTest(TestCase):
    """
    Tests on Profile model.
    """
    def setUp(self):
        self.client = APIClient()

    def test_get_profile(self):
        """
        Test '/api/profile/<uuid:profile_id>'
        """
        data = {
            'username' : 'wololo',
            'password' : 'pwd',
            'birth_date': '1990-4-5'
        }

        signup = self.client.post('/api/signup/', data)

        response = self.client.get(f"/api/profile/{signup.data.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"Profile retrived: {response.data}")

