from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    self.browser.get('http://localhost:8000')

    # 웹 페이지 title과 header가 to-do lists를 표시하고 있다.
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # 그녀는 바로 작업을 추가하기로 한다.
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
    )

    # "공작깃털 구매"라고 텍스트 상자에 입력한다.
    inputbox.send_keys('Buy peacock feathers')

    # 엔터키를 치면 페이지가 갱신되고 to-do 목록에
    # "1: Buy peacock feathers" 아이템이 추가된다.
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
        any(row.text == '1: Buy peacock feathers' for row in rows),
        "New to-do item did not appear in table"
    )

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
    self.fail('Finish the test!')

    # The page updates again, and now shows both items on her list
    # [...]


if __name__ == '__main__':
  unittest.main()
