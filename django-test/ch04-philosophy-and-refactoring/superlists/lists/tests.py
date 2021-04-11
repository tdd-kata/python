from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = home_page(request)
    # print(repr(response.content))
    self.assertTrue(response.content.startswith(b'<html>'))
    self.assertIn(b'<title>To-Do lists</title>', response.content)
    self.assertTrue(response.content.strip().endswith(b'</html>'))

  def test_home_page_returns_correct_html_template(self):
    request = HttpRequest()
    response = home_page(request)
    html = response.content.decode('utf8')
    expected_html = render_to_string('home.html')
    self.assertEqual(html, expected_html)
