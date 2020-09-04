import unittest
import collections 

from cash_register import CashRegister
from main import initialize_register_from_json

class TestCashRegister(unittest.TestCase):

    def test_example1(self):
        register = CashRegister()
        initialize_register_from_json(register, "samples/groceryItems.json")
        cart_items = collections.Counter("ABCD")
        self.assertEqual(register.calculate_total(cart_items), 10.45)

    def test_example2(self):
        register = CashRegister()
        initialize_register_from_json(register, "samples/groceryItems.json")
        cart_items = collections.Counter("DCCBAABB")
        self.assertEqual(register.calculate_total(cart_items), 15.00)

    def test_example3(self):
        register = CashRegister()
        initialize_register_from_json(register, "samples/groceryItems.json")
        cart_items = collections.Counter("ABCD")
        self.assertEqual(register.calculate_total(cart_items), 10.45)
        cart_items = collections.Counter("DCCBAABB")
        self.assertEqual(register.calculate_total(cart_items), 15.00)

    def test_example4(self):
        register = CashRegister()
        initialize_register_from_json(register, "samples/groceryItems.json")
        cart_items = collections.Counter("F")
        with self.assertRaises(Exception): register.calculate_total(cart_items)

    def test_example5(self):
        register = CashRegister()
        initialize_register_from_json(register, "samples/groceryItems.json")
        cart_items = collections.Counter("AAAAAAAAAAAAAAAAAAAAAAA")
        self.assertEqual(register.calculate_total(cart_items), 18.00)

if __name__ == '__main__':
    unittest.main()