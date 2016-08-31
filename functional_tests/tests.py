from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1. cowboy')

        # Again on the page is another text box, inviting her to enter the
        # next word.
        inputbox = self.browser.find_element_by_id('id_new_word')

        # Laura enters the word "loquacious" because she has multiple grade
        # levels in the same classroom
        inputbox.send_keys('loquacious')
        inputbox.send_keys(Keys.ENTER)

        # When the site responds, both words are in the list.
        self.check_for_row_in_list_table('1. cowboy')
        self.check_for_row_in_list_table('2. loquacious')

        # Laura wants to come back to this list later.


        self.fail('Functional tests incomplete')
