from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
      def test_get_req_return_home_page_template(self):
          response = self.client.get('/')
          self.assertTemplateUsed(response, 'home1.html')

  
      def test_Can_post_a_real_value(self):
        response=self.client.post('/',data={"to_do_name":"a new item"})
        self.assertIn("a new item",response.content.decode())
           
