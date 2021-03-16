from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    """Testing home page."""

    def test_root_url_resolver_to_home_page_view(self):
        """Корневой url преобразуется в представление домашней страницы"""
        # Преобразование адреса и нахождение функции представления
        found = resolve('/')
        self.assertEqual(found.func, home_page)
