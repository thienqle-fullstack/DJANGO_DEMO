from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):

    def test_admin_page_status_code(self):
        response = self.client.get('/admin')
        self.assertEquals(response.status_code, 301)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEquals(response.status_code, 404)