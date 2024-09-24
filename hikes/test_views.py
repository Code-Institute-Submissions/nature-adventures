from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Hike


class TestHikeViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser", password="TestPassword"
        )
        self.hike = Hike.objects.create(
            hike_name="Test Hike",
            region="London",
            distance="7",
            description="Great hike",
            author=self.user,
            slug="test-hike",
        )

    def test_render_hike_list_page(self):
        response = self.client.get(reverse(
            'hikes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Hike", response.content)
        self.assertIn(b"London", response.content)
        self.assertIn(b"7", response.content)

    def test_render_hike_info_page(self):
        response = self.client.get(reverse(
            'hike_info',
            args=['test-hike']))
        self.assertEqual(response.status_code, 200)
