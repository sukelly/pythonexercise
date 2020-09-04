import argparse
import collections
import json
from jsonschema import validate

from cash_register import CashRegister
from item import Item, itemSchema
from discount import Discount, discountSchema

def main():
    parser = argparse.ArgumentParser(description="Cash register program: calculate total at checkout")
    parser.add_argument('-items', 
                        '--items',
                        type=str, 
                        help="Set items path, default: %(default)",
                        dest='items_json_path')
    parser.add_argument('-cart',
                        '--cart',
                        type=str,
                        help="Set cart items, default: %(default)",
                        dest='cart')

    args = parser.parse_args()

    register = CashRegister()
    initialize_register_from_json(register, args.items_json_path)
    
    cart_items = collections.Counter(args.cart)
    print(register.calculate_total(cart_items))

def initialize_register_from_json(register: CashRegister, filePath: str):
    all_items = []
    
    with open(filePath, "rb") as myFile:
        all_items = deserialize_data(json.load(myFile))

    register.set_all_items(all_items)

def deserialize_data(data: dict) -> dict:
    items = {}

    for item in data:
        validate(item, itemSchema)
        discount = Discount(int(item.get('discount').get('quantity')), float(item.get('discount').get('cost'))) if item.get('discount') else None
        items[item.get('id')] = Item(item.get('id'), item.get('name'), float(item.get('cost')), discount)

    return items

if __name__ == '__main__':
    main()