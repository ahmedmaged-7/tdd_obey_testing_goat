from django.test import TestCase
from ch5.models import Item
# Create your tests here.
class HomePageTest(TestCase):
      def test_get_req_return_home_page_template(self):
          response = self.client.get('/')
          self.assertTemplateUsed(response, 'home1.html')

  
      def test_Can_post_a_real_value(self):
        response=self.client.post('/',data={"to_do_name":"a new item"})
        self.assertIn("a new item",response.content.decode())
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
             

      def test_get_does_not_affect_db(self):
            self.client.get('/')
            self.assertEqual(Item.objects.all().count(),0)
            
           
