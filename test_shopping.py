
import unittest
from shopping import ShoppingCart, Item


class TestShopping(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.item1 = Item("item1", 10)
        self.item2 = Item("item2", 20)

    def test_add_item(self):
        self.cart.add_item(self.item1)
        self.assertIn(self.item1, self.cart.items)

    def test_remove_item(self):
        self.cart.add_item(self.item1)
        self.cart.remove_item(self.item1)
        self.assertNotIn(self.item1, self.cart.items)

    def test_get_total(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.assertEqual(self.cart.get_total(), 30)
