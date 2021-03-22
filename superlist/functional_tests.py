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
        inputbox.send_keys('By new item')

        # Нажатие enter, обновление страницы
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: By new item' for row in rows),
                "Новый элемент списка не появился в таблице",
                )
        # Созадание еще одного элемента ...
        self.fail('Закончить тест')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
