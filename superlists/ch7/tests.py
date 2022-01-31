from django.test import TestCase
from ch7.models import Item
# Create your tests here.
class HomePageTest(TestCase):
      def test_get_req_return_home_page_template(self):
          response = self.client.get('/')
          self.assertTemplateUsed(response, 'home1.html')

  

                    
class NewListTest(TestCase) :          
      def test_url_redirects_to_list(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(302,response.status_code)
        self.assertEqual(response["location"],"/lists/the_only_list")
