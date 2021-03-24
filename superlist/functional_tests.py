from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя."""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Закрытие браузера"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Можно начать список и получить его позже"""
        #Получим домашнюю страницу
        self.browser.get('http:/localhost:8000')

        #Проверка заголовка
        self.assertIn('To-Do', self.browser.title)
        # Получим элемент заголовка
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                            'Enter a to-do item')

        # Ввод нового пункта
        inputbox.send_keys('Buy a new item')

        # Нажатие enter, обновление страницы
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #Добавление еще одного элемента
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('This is the second element')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy a new item', [row.text for row in rows])
        self.assertIn('2: This is the second element', [row.text for row in rows])

        # Созадание еще одного элемента ...
        # Сайт запоминает текущий список пользователя
        self.fail('Закончить тест')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
