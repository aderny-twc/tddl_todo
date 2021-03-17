from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

#from views import home_page
from lists.views import home_page


class HomePageTest(TestCase):
    """Testing home page."""

    def test_root_url_resolver_to_home_page_view(self):
        """Корневой url преобразуется в представление домашней страницы"""
        # Преобразование адреса и нахождение функции представления
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        """Домашняя страница возвращает правильный html"""
        # Объект при запросе страницы
        request = HttpRequest()
        # Передача представлению
        response = home_page(request)
        # Извлечение содержимого
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
