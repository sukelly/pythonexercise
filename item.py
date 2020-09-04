from discount import Discount, discountSchema

class Item:
    def __init__(self, id: str, name: str, cost: float, discount: Discount=None):
        self.id = id
        self.name = name
        self.cost = cost
        self.discount = discount

itemSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "cost": {"type": "number"},
        "discount": discountSchema,
    },
    "required": ["id", "name", "cost"]
}