import unittest
from employee import Employee
import os

os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_11\\11.3')

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.new_employee = Employee ('John','Fobos',100_000)

    def test_give_default_raise(self):
        self.new_employee.get_raise()
        self.assertEqual(self.new_employee.current_salary,105_000)

    def test_give_custom_raise(self):
        self.new_employee.get_raise(10_000)
        self.assertEqual(self.new_employee.current_salary,110_000)
    
if __name__ == '__main__':
    unittest.main()