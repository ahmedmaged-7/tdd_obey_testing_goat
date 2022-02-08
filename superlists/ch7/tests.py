from django.test import TestCase
from ch7.models import Item,List
# Create your tests here.
class HomePageTest(TestCase):
      def test_get_req_return_home_page_template(self):
          response = self.client.get('/')
          self.assertTemplateUsed(response, 'home1.html')
  

      def test_save_post_Value_in_database(self):
            items_stored=Item.objects.all().count()
            response=self.client.post('/lists/10/',data={"to_do_name":"a new item"})
            print(f'the content is {response.content.decode()}')
            self.assertEqual(items_stored+1,Item.objects.all().count())
             

      def test_get_request_does_not_affect_db(self):
            self.client.get('/')
            self.assertEqual(Item.objects.all().count(),0)

     

      def test_we_get_redirected_after_post(self):
            response=self.client.post('/',data={"to_do_name":"HEX"})
            self.assertEqual(response.status_code,302)
       
      def test_reteriving_from_unit_test_Database_Works(self):
            list_=List.objects.create()
            Item.objects.create(to_do_list_value="HEX",list=list_)            
            self.assertEqual(Item.objects.first().to_do_list_value,"HEX")
            self.assertIn("HEX",self.client.get(f'/lists/{list_.id}/').content.decode())

                    
      def test_url_redirects_to_list(self):
        response = self.client.post('/lists/2/', data={'item_text': 'A new list item'})
        self.assertEqual(302,response.status_code)
        #self.assertEqual(response["location"],"/lists/the_only_list/")
      def test_list_exists_And_returns_the_items(self):
            list_=List.objects.create()            
            Item.objects.create(to_do_list_value="item1",list=list_)
            Item.objects.create(to_do_list_value="item2",list=list_)

            
            response = self.client.get(f'/lists/{list_.id}/')
            self.assertEqual(200,response.status_code)


            self.assertContains(response,"item1")#this is a new command instead of decode the content
            self.assertContains(response,"item2")
      def test_Assert_tha_list_uses_list_template(self):
            list_=List.objects.create()                        
            response = self.client.get(f'/lists/{list_.id}/')
            self.assertTemplateUsed(response,"list.html")
            
class NewListTest(TestCase) :

           def test_can_Save_post_request(self):
                 response=self.client.post("/lists/new/",data={'to_do_name': 'A new list item'})
                 self.assertEqual(Item.objects.count(),1)
                 item=Item.objects.first()
                 self.assertEqual(item.to_do_list_value,"A new list item")
                 
           def test_redirects_After_post(self):
                 list_=List.objects.create()            
                 response=self.client.post(f"/lists/{list_.id}/",data={'item_text': 'A new list item'})
                 self.assertRedirects(response,f'/lists/{list_.id}/')
class ListAndItemModelTest(TestCase):
      def test_Saving_reteriveng_items(self):
            testing_list=List() #he choose list_that name to diffrentiate from python list i choosed another cuz list_ iis ugly
            testing_list.save()

            first_item=Item()
            first_item.to_do_list_value="first item "
            first_item.list=testing_list
            first_item.save()

            second_item=Item()
            second_item.to_do_list_value="second item "
            second_item.list=testing_list
            second_item.save()

            saved_items=Item.objects.all()
            self.assertEqual(saved_items.count(),2)

            [first,second]=saved_items
            self.assertEqual(first.to_do_list_value,"first item ")
            self.assertEqual(first.list,testing_list)
            self.assertEqual(second.to_do_list_value,"second item ")
            self.assertEqual(second.list,testing_list)
            
      def test_uses_list_template(self):
            list_=List.objects.create()
            response=self.client.get(f'/lists/{list_.id}/')
            self.assertTemplateUsed(response,'list.html')
            
      def test_seprate_lists_items_are_not_Same(self): #this is how to format unit test start with   envirmonent \n action \n result
            correct_list=List.objects.create()
            other_list=List.objects.create()
            Item.objects.create(to_do_list_value="first in correct list",list=correct_list)
            Item.objects.create(to_do_list_value="second in correct list",list=correct_list)
            Item.objects.create(to_do_list_value="first in other list",list=other_list)
            Item.objects.create(to_do_list_value="second in other list",list=other_list)

            response=self.client.get(f'/lists/{correct_list.id}/')

            self.assertContains(response,"first in correct list")
            self.assertContains(response,"second in correct list")
            self.assertNotContains(response,"first in other list")
            self.assertNotContains(response,"second in other list")
