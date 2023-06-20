from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class TagsTest(TestCase):
    def set_up(self):
        self.client = APIClient()

    def test_list_tags(self):
        """
        Test rout '/api/tags/'
        """
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
