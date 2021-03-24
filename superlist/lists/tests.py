from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

#from views import home_page
from lists.views import home_page


class HomePageTest(TestCase):
    """Testing home page."""

    def test_root_url_resolver_to_home_page_view(self):
        """Корневой url преобразуется в представление домашней страницы"""
        # Преобразование адреса и нахождение функции представления
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_test_server_django_returns_correct_html(self):
        """Home page returns right html"""
        response = self.client.get('/')
        #html = response.content.decode('utf8')
        #self.assertTrue(html.startswith('<html>'))
        #self.assertIn('<title>To-Do lists</title>', html)
        #self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        """Test: saving POST-request."""
        response = self.client.post('/',
                                    data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')
