from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starts_a_list_and_retrieves_it_later(self):
        # get the homepage
        self.browser.get('http://localhost:8000')
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
