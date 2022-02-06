from django.test import TestCase
from ch7.models import Item
# Create your tests here.
class HomePageTest(TestCase):
      def test_get_req_return_home_page_template(self):
          response = self.client.get('/')
          self.assertTemplateUsed(response, 'home1.html')
  
        
      def test_make_orm_and_reterive_the_to_do_list_stored(self):
            item1=Item()
            item1.to_do_list_value="text1"
            item1.save()
            item2=Item()
            item2.to_do_list_value="text2"
            item2.save()
            items_stored=Item.objects.all()#remmember to put objects when calling
            self.assertEqual(items_stored.count(),2)
            self.assertEqual(items_stored[0].to_do_list_value,"text1")
            self.assertEqual(items_stored[1].to_do_list_value,"text2")

      def test_save_post_Value_in_database(self):
            items_stored=Item.objects.all().count()
            response=self.client.post('/',data={"to_do_name":"a new item"})
            self.assertEqual(items_stored+1,Item.objects.all().count())
             

      def test_get_request_does_not_affect_db(self):
            self.client.get('/')
            self.assertEqual(Item.objects.all().count(),0)

      def test_we_have_a_same_value_in_database(self):
            response=self.client.post('/',data={"to_do_name":"HEX"})
            self.assertEqual("HEX",Item.objects.first().to_do_list_value)

      def test_we_get_redirected_after_post(self):
            response=self.client.post('/',data={"to_do_name":"HEX"})
            self.assertEqual(response.status_code,302)
       
      def depracated_test_reteriving_from_unit_test_Database_Works(self):
            Item.objects.create(to_do_list_value="HEX")            
            self.assertEqual(Item.objects.first().to_do_list_value,"HEX")
            self.assertIn("HEX",self.client.get('/').content.decode())

  

                    
class NewListTest(TestCase) :          
      def test_url_redirects_to_list(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(302,response.status_code)
        #self.assertEqual(response["location"],"/lists/the_only_list/")
      def test_list_exists_And_returns_the_items(self):
            Item.objects.create(to_do_list_value="item1")
            Item.objects.create(to_do_list_value="item2")

            
            response = self.client.get('/lists/the_only_list/')
            self.assertEqual(200,response.status_code)


            self.assertContains(response,"item1")#this is a new command instead of decode the content
            self.assertContains(response,"item2")
      def test_Assert_tha_list_uses_list_template(self):
            
            response = self.client.get('/lists/the_only_list/')
            self.assertTemplateUsed(response,"list.html")
