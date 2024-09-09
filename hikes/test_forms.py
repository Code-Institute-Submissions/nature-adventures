from django.test import TestCase
from .forms import CreateHikeForm

# Create your tests here.

class TestCreateHikeForm(TestCase):

    def test_form_is_valid(self):
        create_hike_form = CreateHikeForm(
            {'hike_name': 'Test Hike',
            'region': 'London',
            'distance': '7',
            'description': 'This is a great hike!',})
        self.assertTrue(create_hike_form.is_valid()),

    def test_hike_name_not_valid(self):
        create_hike_form = CreateHikeForm(
            {'hike_name': '',
            'region': 'London',
            'distance': '7',
            'description': 'Great hike',})
        self.assertFalse(create_hike_form.is_valid()),
    
    def test_region_not_valid(self):
        create_hike_form = CreateHikeForm(
            {'hike_name': 'Test Hike',
            'region': 'Helsinki',
            'distance': '7',
            'description': 'Great hike',})
        self.assertFalse(create_hike_form.is_valid()),

    def test_distance_not_valid(self):
        create_hike_form = CreateHikeForm(
            {'hike_name': 'Test Hike',
            'region': 'London',
            'distance': '0',
            'description': 'Great hike',})
        self.assertFalse(create_hike_form.is_valid()),

    def test_description_not_valid(self):
        create_hike_form = CreateHikeForm(
            {'hike_name': 'Test Hike',
            'region': 'London',
            'distance': '7',
            'description': '',})
        self.assertFalse(create_hike_form.is_valid()),
        