import unittest
from city_functions import get_city_function
import os

os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_11\\11.1')

class NamesTestCase(unittest.TestCase):
    '''Тесты для "city_functions.py" '''
    def test_city_country(self):
        formatted_name = get_city_function('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')

if __name__ == '__main__':
    unittest.main()