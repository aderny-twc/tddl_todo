from selenium import webdriver
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
        #Генерация сообщения ошибки
        self.fail('End of test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
