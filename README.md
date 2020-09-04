Dependencies:

1. Python3

Run program using cli 

python3 main.py --items <json_file> --cart <cart_items>

parameters: 

1. json_file: .json file

Schema: 
{
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "cost": {"type": "number"},
        "discount": {
            "type": "object",
            "properties": {
                "quantity": {"type": "number"},
                "cost": {"type": "number"}
            },
            "required": ["quantity", "cost"]
        }
    "required": ["id", "name", "cost"]
}

See samples/groceryItems.json for an example

2. cart_items: string

Example run:

git clone 

cd pythonexercise

python3 main.py --items samples/groceryItems.json --cart "ABCD"

Run all tests

python3 test_module.py

Note: Examples included in instruction are included in test_module.py