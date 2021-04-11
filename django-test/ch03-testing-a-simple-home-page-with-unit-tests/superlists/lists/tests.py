# from django.urls import resolve # 1.7,2.0+
from django.core.urlresolvers import resolve # 1.8 only
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)
