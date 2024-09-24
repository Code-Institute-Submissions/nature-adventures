from django.test import TestCase
from django.urls import reverse, resolve
from .views import HikesList
from .views import hike_info, new_hike, update_hike, delete_hike, like_hike


class TestUrls(TestCase):

    def test_HikesList_resolves(self):
        url = reverse('hikes')
        self.assertEqual(resolve(url).func.view_class, HikesList)

    def test_hike_info_resolves(self):
        url = reverse('hike_info', args=['random-slug'])
        self.assertEqual(resolve(url).func, hike_info)

    def test_new_hike_resolves(self):
        url = reverse('new_hike')
        self.assertEqual(resolve(url).func, new_hike)

    def test_update_hike_resolves(self):
        url = reverse('update_hike', args=['random-slug'])
        self.assertEqual(resolve(url).func, update_hike)

    def test_delete_hike_resolves(self):
        url = reverse('delete_hike', args=['random_slug'])
        self.assertEqual(resolve(url).func, delete_hike)

    def test_like_hike_resolves(self):
        url = reverse('like_hike', args=['random_slug'])
        self.assertEqual(resolve(url).func, like_hike)
