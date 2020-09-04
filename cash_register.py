import unittest
from jsonschema import validate

from item import Item, itemSchema

class CashRegister:
    def __init__(self):
        self.set_all_items([])

    def set_all_items(self, all_items):
        self._all_items = all_items

    def get_all_items(self) -> list:
        return self._all_items
        
    def calculate_total(self, cart_items: dict) -> float:
        cart_total = 0

        for item_id, quantity in cart_items.items():
            if item_id not in self._all_items:
                raise Exception("Item not found")

            item = self._all_items[item_id]

            if item.discount:
                item_total = (quantity // item.discount.quantity)*(item.discount.cost) + (quantity % item.discount.quantity)*(item.cost)
            else:
                item_total = (quantity)*(item.cost)

            cart_total += item_total

        return cart_total