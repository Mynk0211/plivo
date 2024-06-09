from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Message

class MessageTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.message = Message.objects.create(
            account_id="account_1",
            sender_number="1234567890",
            receiver_number="0987654321"
        )

    def test_get_messages(self):
        url = reverse('get_messages', args=['account_1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_message(self):
        url = reverse('create_message')
        data = {
            "account_id": "account_2",
            "sender_number": "1111111111",
            "receiver_number": "2222222222"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_messages(self):
        url = reverse('search_messages')
        response = self.client.get(url, {'sender_number': '1234567890'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

