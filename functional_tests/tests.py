from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_starts_a_list_and_retrieves_it_later(self):
        # get the homepage
        self.browser.get(self.live_server_url)

        # notice page title and header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User invited to enter to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When you hit enter, taken to new url
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # get the text box inviting to add a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys( 'Use peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)
        #
        time.sleep(5)

        # # find the item
        self.check_for_row_in_list_table('2: Use peacock feathers to make fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # quit to wipe out all previous information
        self.browser.quit()
        self.browser = webdriver.Firefox()

#
#         # part 2
#         # Another person visits the home page
#         # Previous list is wiped out
#
#
#
#         # next step
#         self.fail("Finish the test")
#         self.browser.get(self.live_server_url)
#         page_text = self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peackcock feathers', page_text)
#         self.assertNotIn('make a fly', page_text)
#
#         # Start a new list and enter new items
#
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Buy milk')
#         inputbox.send_keys(Keys.ENTER)
#
#         # Assign a unique URL to this list--name "francis"
#         francis_list_url = self.browser.current_url
#         self.assertRegex(francis_list_url, '/lists/.+')
#         self.assertNotEqual(francis_list_url, edith_list_url)
#
#         # Make sure there's no trace of previous list
#         page_text = self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_text)
#         self.assertIn('Buy milk', page_text)
#
