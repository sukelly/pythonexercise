class Discount:
    def __init__(self, quantity: int, cost: float):
        self.quantity = quantity
        self.cost = cost

discountSchema = {
    "type": "object",
    "properties": {
        "quantity": {"type": "number"},
        "cost": {"type": "number"}
    },
    "required": ["quantity", "cost"]
}