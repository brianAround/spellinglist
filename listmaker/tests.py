from django.core.urlresolvers import resolve
from django.test import TestCase
from listmaker.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_reolves_to_home_page_view(self):
        found =resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.html')

    
