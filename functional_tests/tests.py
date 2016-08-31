from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()



    def test_page_shows_valid_html(self):
        # Laura follows a link from her email about a spelling list management
        # site and gets to the home page.
        self.browser.get(self.live_server_url)
        # the site title reassures her that she is in the right place
        self.assertIn('Spelling List Helper', self.browser.title)

        # Laura notices that she has a text box available to enter the first word
        # of her spelling list.
        inputbox = self.browser.find_element_by_id('id_new_word')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter the first word'
        )

        # She enters the word "cowboy"
        inputbox.send_keys('cowboy')

        # When she hits enter the page displays her new word in a list.


        # At the end of the list is another text box, inviting her to enter the
        # next word.


        self.fail('Functional tests incomplete')
