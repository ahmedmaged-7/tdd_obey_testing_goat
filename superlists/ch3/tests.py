from django.test import TestCase
from django.urls import resolve
from ch3.views import home_page
from django.http import HttpResponse
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_contains_to_Do_list(self):
       # found=resolve('/')
        request=HttpResponse()
        found=home_page(request)
        html=found.content.decode("utf-8")
        self.assertIn("to do list",html,html)
        
           
        
