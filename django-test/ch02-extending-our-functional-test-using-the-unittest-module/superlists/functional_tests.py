from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

  # 테스트 전 실행
  def setUp(self):
    self.browser = webdriver.Firefox()

  # 테스트 후 실행. 테스트에 에러가 발생해도 실행된다.
  def tearDown(self):
    self.browser.quit()

  # `test`라는 이름으로 시작하는 모든 메소드는 test runner에 의해 실행된다.
  def test_can_start_a_list_and_retrieve_it_later(self):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    self.browser.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # She is invited to enter a to-do item straight away

    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very methodical)

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep


# 파이썬 스크립트가 다른 스크립트에 임포트된 것이 아니라 커맨드라인을 통해 실행됐다는 것을 확인하는 코드
if __name__ == '__main__':
  unittest.main()
