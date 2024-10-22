# Unit Testing
from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        self.assertEqual(user.username, 'testuser')

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass123', eamil='testuser@test.com', nickname='usernickname')
        self.assertEqual(user.username, 'testuser')