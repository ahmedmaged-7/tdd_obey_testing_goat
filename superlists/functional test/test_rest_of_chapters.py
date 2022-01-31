from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

MAX_WAIT=5 #max time to wait for a row to appear
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

     

    def wait_for_row_in_table(self,table_iD,row_text):
         start_time=time.time()
         while(True):
           try:
             
             table = self.browser.find_element_by_id(table_iD)
             rows = table.find_elements_by_tag_name('tr')
             self.assertIn(row_text, [row.text for row in rows])
             return
           except(AssertionError,WebDriverException)as e:
               if(time.time()-start_time >MAX_WAIT):
                   raise e
               time.sleep(0.3)     
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)#it is live not life

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('the_to_do_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox = self.browser.find_element_by_id('the_to_do_item')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_table("id_new_table","1: Buy peacock feathers")
 
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table

        inputbox = self.browser.find_element_by_id('the_to_do_item')


        inputbox.send_keys('use peacok feathers to make a fly')        
        inputbox.send_keys(Keys.ENTER)

        
        self.wait_for_row_in_table("id_new_table","2: use peacok feathers to make a fly")
       
       

    def test_multiple_users_Each_has_a_his_own_list_ch7(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('the_to_do_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_table("id_new_table","1: Buy peacock feathers")
        inputbox = self.browser.find_element_by_id('the_to_do_item')
        inputbox.send_keys('use peacok feathers to make a fly')        
        inputbox.send_keys(Keys.ENTER)

        
        self.wait_for_row_in_table("id_new_table","2: use peacok feathers to make a fly")
       
        
        edith_url=self.browser.current_url
        self.assertRegex(edith_url,'/lists/.+')
        print(edith_url)
        #a new user starts a session wants to add his items

        #a new hand touches the beacon :)
        
        self.browser.quit()
        self.browser=webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element_by_id("body").text
        ##the page should be empty
        self.assertNotIn("1: Buy peacock feathers",page_text)
        
        inputbox = self.browser.find_element_by_id('the_to_do_item')
        inputbox.send_keys('buy milk')        
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_table("id_new_table","1: buy milk")
        
        ##check that page francsis not the one for edith
        francis_url=self.browser.current_url
        self.assertRegex(francis_url,'/lists/.+')
        self.assertNotEqual(edith_url,francis_url)
        page_text=self.browser.find_Element_by_id("body").text
        self.assertNotIn("1: Buy peacock feathers",page_text)
        self.assertIn("1: buy milk",page_text)
        


