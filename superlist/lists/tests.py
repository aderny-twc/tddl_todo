from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

#from views import home_page
from lists.views import home_page
from lists.models import Item


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

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        #self.assertIn('A new list item', response.content.decode())
        #self.assertTemplateUsed(response, 'lists/home.html')

    def test_only_saves_items_when_necessary(self):
        """Тест: сохранять элементы, только когда это нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    """Тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элеметов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')









