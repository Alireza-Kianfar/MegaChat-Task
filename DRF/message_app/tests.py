from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Message


class MessageApiTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		User = get_user_model()
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.client.force_authenticate(user=self.user)

	def test_create_and_list(self):
		# Create a message
		resp = self.client.post('/api/messages/', {'text': 'hello world'}, format='json')
		self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
		self.assertIn('id', resp.data)

		# List messages
		resp2 = self.client.get('/api/messages/')
		self.assertEqual(resp2.status_code, status.HTTP_200_OK)
		self.assertIsInstance(resp2.data, list)
		self.assertGreaterEqual(len(resp2.data), 1)

	def test_ordering_by_created_at(self):
		Message.objects.create(text='first')
		Message.objects.create(text='second')
		resp = self.client.get('/api/messages/')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertIsInstance(resp.data, list)
		texts = [m['text'] for m in resp.data]
		# Newest first
		self.assertEqual(texts[0], 'second')
