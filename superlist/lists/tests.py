from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    """Тест на токсичность"""

    def test_bad_maths(self):
        """Неправильные математические расчеты"""
        self.assertEqual(1 + 1, 3)