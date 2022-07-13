import unittest
from city_functions import get_city_function
import os

os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_11\\11.2')

class assertEqual(unittest.TestCase):
    '''Тесты для 'city_functions.py' '''
    def test_city_country(self):
        formatted_name = get_city_function('santiago','chile')
        self.assertEqual(formatted_name,'Santiago Chile')

    def test_city_country(self):
        formatted_name = get_city_function('santiago','chile',5000)
        self.assertEqual(formatted_name,'Santiago Chile - population: 5000')

if __name__ == '__main__':
    unittest.main()